#!/usr/bin/env python3
"""Pi2W Display Service - webhook + scheduled refreshes using uvicorn/starlette."""

import asyncio
import logging
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path

import httpx
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse, Response
from starlette.routing import Route

# Path to latest displayed image (saved by display_client.py)
LATEST_IMAGE_PATH = Path(__file__).parent / "latest.png"

# Load .env file if present
env_file = Path(__file__).parent / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

# Configuration from environment
PORT = int(os.environ.get("PORT", "8080"))
MIN_INTERVAL = int(os.environ.get("MIN_INTERVAL", "1800"))  # 30 minutes
SCHEDULE_INTERVAL = int(os.environ.get("SCHEDULE_INTERVAL", "1800"))  # 30 minutes
QUIET_HOURS_START = int(os.environ.get("QUIET_HOURS_START", "0"))  # midnight
QUIET_HOURS_END = int(os.environ.get("QUIET_HOURS_END", "7"))  # 7am

HA_URL = os.environ.get("HA_URL", "http://localhost:8123")
HA_TOKEN = os.environ.get("HA_TOKEN")
SENSOR = os.environ.get("HA_SENSOR", "binary_sensor.office_occupancy")
SERVER_URL = os.environ.get("SERVER_URL", "http://192.168.0.148/pi2w-server")

if not HA_TOKEN:
    raise RuntimeError("HA_TOKEN environment variable is required")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# State
last_refresh = 0
last_refresh_time: datetime | None = None
refresh_count = 0
skipped_empty = 0  # Skipped due to no occupancy
skipped_quiet = 0  # Skipped during quiet hours (no occupancy)
service_start_time = datetime.now()


def is_quiet_hours() -> bool:
    hour = datetime.now().hour
    return QUIET_HOURS_START <= hour < QUIET_HOURS_END


async def check_occupancy() -> bool:
    """Check if office is occupied via Home Assistant API."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{HA_URL}/api/states/{SENSOR}",
                headers={"Authorization": f"Bearer {HA_TOKEN}"},
                timeout=10.0
            )
            resp.raise_for_status()
            return resp.json().get("state") == "on"
    except Exception as e:
        logger.error(f"Occupancy check failed: {e}")
        return False


def do_refresh(source: str = "unknown", force: bool = False) -> bool:
    """Trigger display refresh.

    Args:
        source: Label for logging
        force: If True, skip the MIN_INTERVAL check
    """
    global last_refresh, last_refresh_time, refresh_count
    now = time.time()
    elapsed = now - last_refresh

    if not force and elapsed < MIN_INTERVAL:
        logger.info(f"[{source}] Skipped: last refresh {int(elapsed)}s ago")
        return False

    logger.info(f"[{source}] Refreshing display...")
    last_refresh = now
    last_refresh_time = datetime.now()
    refresh_count += 1

    subprocess.Popen([
        "/usr/bin/python3",
        str(Path(__file__).parent / "display_client.py"),
        "--server", SERVER_URL,
        "--save-path", str(LATEST_IMAGE_PATH),
    ])
    return True


async def scheduler():
    """Background task for scheduled refreshes."""
    global skipped_empty, skipped_quiet
    logger.info("Scheduler started")

    # Initial refresh at startup if occupied
    await asyncio.sleep(5)
    if await check_occupancy():
        do_refresh("startup")

    while True:
        await asyncio.sleep(SCHEDULE_INTERVAL)

        occupied = await check_occupancy()

        if is_quiet_hours():
            if occupied:
                # Someone's there during quiet hours - still refresh!
                logger.info("[scheduled] Quiet hours but occupied - refreshing anyway")
                do_refresh("scheduled-quiet")
            else:
                skipped_quiet += 1
                logger.info(f"[scheduled] Quiet hours & empty, skipping (total: {skipped_quiet})")
            continue

        if not occupied:
            skipped_empty += 1
            logger.info(f"[scheduled] Office empty, skipping (total: {skipped_empty})")
            continue

        do_refresh("scheduled")


# Routes
async def health(request):
    return PlainTextResponse("OK")


async def status(request):
    """Detailed status endpoint."""
    image_exists = LATEST_IMAGE_PATH.exists()
    image_mtime = None
    if image_exists:
        image_mtime = datetime.fromtimestamp(LATEST_IMAGE_PATH.stat().st_mtime).isoformat()

    # Build status summary: "5 shown, 2 empty, 1 night"
    status_parts = [f"{refresh_count} shown"]
    if skipped_empty > 0:
        status_parts.append(f"{skipped_empty} empty")
    if skipped_quiet > 0:
        status_parts.append(f"{skipped_quiet} night")
    status_summary = ", ".join(status_parts)

    return JSONResponse({
        "status": status_summary,
        "timestamp": datetime.now().isoformat(),
        "service_uptime_seconds": int((datetime.now() - service_start_time).total_seconds()),
        "quiet_hours": is_quiet_hours(),
        "last_refresh": last_refresh_time.isoformat() if last_refresh_time else None,
        "refresh_count": refresh_count,
        "skipped_empty": skipped_empty,
        "skipped_quiet": skipped_quiet,
        "latest_image": {
            "available": image_exists,
            "modified_at": image_mtime,
        },
    })


async def refresh_endpoint(request):
    """Manual refresh via webhook - always allowed (even during quiet hours)."""
    if do_refresh("webhook"):
        return PlainTextResponse("Refresh triggered")
    else:
        return PlainTextResponse("Skipped (too soon)")


async def latest_art(request):
    """Serve the latest displayed image."""
    if not LATEST_IMAGE_PATH.exists():
        return PlainTextResponse("No image available", status_code=404)

    image_data = LATEST_IMAGE_PATH.read_bytes()
    mtime = datetime.fromtimestamp(LATEST_IMAGE_PATH.stat().st_mtime)

    return Response(
        content=image_data,
        media_type="image/png",
        headers={
            "X-Generated-At": mtime.isoformat(),
            "Cache-Control": "public, max-age=60",
        },
    )


app = Starlette(
    debug=False,
    routes=[
        Route("/health", health),
        Route("/status", status),
        Route("/refresh", refresh_endpoint),
        Route("/art/latest", latest_art),
    ],
    on_startup=[lambda: asyncio.create_task(scheduler())]
)


if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="warning")
