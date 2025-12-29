#!/usr/bin/env python3
"""
Pi2W Display Client - Fetches content from server and displays on Inky Impression.
"""

import io
import sys
import time
import argparse
import logging
from pathlib import Path

import httpx
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Display configuration (Inky Impression 7.3" Spectra - E673 driver)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480

# Try to import inky - will fail on non-Pi systems
try:
    from inky.auto import auto
    INKY_AVAILABLE = True
except ImportError:
    INKY_AVAILABLE = False
    logger.warning("Inky library not available - running in simulation mode")


# Known display color configurations
DISPLAY_PALETTES = {
    "multi": 7,      # 7-color ACeP (older)
    "spectra6": 6,   # Spectra 6 (2025 edition) - black, white, red, yellow, green, blue
    "red": 3,        # Black, white, red
    "yellow": 3,     # Black, white, yellow  
    "black": 2,      # Black, white only
}


class InkyDisplay:
    """Wrapper for Inky Impression display."""

    def __init__(self, simulate: bool = False):
        self.simulate = simulate or not INKY_AVAILABLE

        if not self.simulate:
            self.display = auto()
            self.width = self.display.WIDTH
            self.height = self.display.HEIGHT
            self.colour = getattr(self.display, 'colour', 'multi')
            
            # E673 driver = Spectra 6 (6 colors, no orange)
            module = type(self.display).__module__
            if 'e673' in module.lower() or 'spectra' in module.lower():
                self.num_colors = 6
            else:
                self.num_colors = DISPLAY_PALETTES.get(self.colour, 7)
            
            logger.info(f"Display detected: {module}, colours={self.num_colors}")
        else:
            self.display = None
            self.width = DISPLAY_WIDTH
            self.height = DISPLAY_HEIGHT
            self.colour = "multi"
            self.num_colors = 7
            logger.info("Running in simulation mode")

    def show(self, image: Image.Image, save_path: Path | None = None):
        """Display image on screen and optionally save to file."""
        # Ensure correct size
        if image.size != (self.width, self.height):
            image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)

        # Always save latest image for serving via HTTP
        if save_path:
            image.save(save_path)
            logger.info(f"Image saved to {save_path}")

        if self.simulate:
            # Save to file for preview
            output_path = Path("/tmp/inky_preview.png")
            image.save(output_path)
            logger.info(f"Simulation: Image saved to {output_path}")
        else:
            logger.info("Updating display (this takes ~30 seconds)...")
            self.display.set_image(image)
            self.display.show()
            logger.info("Display updated!")


class ContentClient:
    """Client to fetch content from Pi2W server."""

    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip("/")
        self.client = httpx.Client(timeout=120.0)  # Long timeout for AI generation

    def health_check(self) -> bool:
        """Check if server is available."""
        try:
            response = self.client.get(f"{self.server_url}/health")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False

    def get_art(
        self, 
        width: int,
        height: int,
        colors: int = 7,
        style: str | None = None, 
        prompt: str | None = None,
    ) -> Image.Image:
        """Fetch AI-generated art from server."""
        params = {"width": width, "height": height, "colors": colors}
        if style:
            params["style"] = style
        if prompt:
            params["prompt"] = prompt

        logger.info(f"Requesting art from server ({width}x{height}, {colors} colors)...")
        response = self.client.get(f"{self.server_url}/art", params=params)
        response.raise_for_status()

        # Log metadata from headers
        time_of_day = response.headers.get("X-Time-Of-Day", "unknown")
        logger.info(f"Received art for time of day: {time_of_day}")

        # Parse image
        image = Image.open(io.BytesIO(response.content))
        return image

    def close(self):
        """Close the HTTP client."""
        self.client.close()


def main():
    parser = argparse.ArgumentParser(description="Pi2W Display Client")
    parser.add_argument(
        "--server",
        default="http://192.168.0.1:8000",  # Default server address
        help="Server URL (e.g., http://192.168.0.1:8000)"
    )
    parser.add_argument(
        "--style",
        help="Art style (e.g., watercolor, minimalist, impressionist)"
    )
    parser.add_argument(
        "--prompt",
        help="Custom prompt for art generation"
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Run in simulation mode (don't use actual display)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=0,
        help="Refresh interval in minutes (0 = one-shot)"
    )
    parser.add_argument(
        "--save-path",
        type=Path,
        default=Path(__file__).parent / "latest.png",
        help="Path to save latest displayed image"
    )

    args = parser.parse_args()

    # Initialize display
    display = InkyDisplay(simulate=args.simulate)

    # Initialize client
    client = ContentClient(args.server)

    try:
        # Check server health
        if not client.health_check():
            logger.error("Server is not available")
            sys.exit(1)

        while True:
            try:
                # Fetch and display art
                image = client.get_art(
                    width=display.width,
                    height=display.height,
                    colors=display.num_colors,
                    style=args.style,
                    prompt=args.prompt,
                )
                display.show(image, save_path=args.save_path)

                if args.interval <= 0:
                    break

                logger.info(f"Sleeping for {args.interval} minutes...")
                time.sleep(args.interval * 60)

            except httpx.HTTPError as e:
                logger.error(f"HTTP error: {e}")
                if args.interval <= 0:
                    sys.exit(1)
                time.sleep(60)  # Wait a minute before retrying

            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                break

    finally:
        client.close()


if __name__ == "__main__":
    main()
