# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Content server for Raspberry Pi Zero 2W with Inky Impression 7.3" Spectra e-ink display. Server runs on devsrv (192.168.0.148), generates content via OpenAI DALL-E, and Pi client fetches and displays it every 30 minutes.

## Architecture

```
┌─────────────────────────┐         ┌─────────────────────────┐
│  devsrv (Ubuntu)        │  HTTP   │  Raspberry Pi Zero 2W   │
│  192.168.0.148          │◄───────►│  pi2w.local             │
│  Nginx → FastAPI        │         │  piroot@pi2w.local      │
│  /pi2w-server/*         │         │  ~/pi2w-client/         │
│                         │         │  :8080 webhook listener │
│  Home Assistant :8123   │────────►│                         │
│  (Docker container)     │ webhook │                         │
└─────────────────────────┘         └─────────────────────────┘
         │                                   │
         │ occupancy                         ▼
         │ sensor                  ┌─────────────────────────┐
         ▼                         │  Inky Impression 7.3"   │
┌─────────────────────────┐        │  800x480, 7-color       │
│  binary_sensor.         │        │  E673 driver            │
│  office_occupancy       │        └─────────────────────────┘
└─────────────────────────┘
```

### Refresh Logic

The Pi client (`pi2w-webhook.service`) handles display refreshes via:

1. **Home Assistant webhook**: When `binary_sensor.office_occupancy` turns on, HA calls `http://pi2w.local:8080/refresh`
2. **Scheduled refresh**: Every 30 minutes, checks occupancy before refreshing
3. **Startup refresh**: On service start, refreshes if office is occupied

Constraints:
- **Quiet hours**: No refreshes between midnight and 7am
- **Rate limit**: Minimum 30 minutes between refreshes
- **Occupancy check**: Scheduled refreshes skip if office is empty

## Deployment

### Server (devsrv - 192.168.0.148)

**Location**: `~/pi2w-server/`
**URL**: `http://192.168.0.148/pi2w-server/`
**Service**: `pi2w-server.service`

**Nginx**: Configured in `/etc/nginx/sites-available/default` with a location block:
```nginx
location /pi2w-server/ {
    proxy_pass http://127.0.0.1:8000/;
    proxy_read_timeout 120s;
}
```
⚠️ **DO NOT create a separate nginx site** - the server has other routes. Only add location blocks to the existing `default` config.

```bash
# Deploy server code
rsync -av --exclude '__pycache__' --exclude '.venv' pi2w/ 192.168.0.148:~/pi2w-server/pi2w/
scp server.py 192.168.0.148:~/pi2w-server/

# Restart service
ssh 192.168.0.148 "sudo systemctl restart pi2w-server"

# Check status
ssh 192.168.0.148 "sudo systemctl status pi2w-server"
ssh 192.168.0.148 "sudo journalctl -u pi2w-server -f"

# Test endpoints
curl http://192.168.0.148/pi2w-server/health
curl http://192.168.0.148/pi2w-server/art/preview
curl http://192.168.0.148/pi2w-server/art -o test.png
```

### Pi Client (pi2w.local)

**Location**: `~/pi2w-client/`
**User**: `piroot` (SSH key auth)
**Service**: `pi2w-webhook.service` (HTTP listener + scheduler)
**Config**: `~/pi2w-client/.env` (contains HA token - not in repo)

```bash
# Deploy client code
scp pi_client/display_client.py pi_client/webhook_listener.py piroot@pi2w.local:~/pi2w-client/

# Service management
ssh piroot@pi2w.local "sudo systemctl restart pi2w-webhook"
ssh piroot@pi2w.local "sudo systemctl status pi2w-webhook"
ssh piroot@pi2w.local "sudo journalctl -u pi2w-webhook -f"

# Test webhook
curl http://pi2w.local:8080/health
curl http://pi2w.local:8080/refresh

# Manual display refresh
ssh piroot@pi2w.local "python3 ~/pi2w-client/display_client.py --server http://192.168.0.148/pi2w-server"
```

**Pi client `.env` file** (`~/pi2w-client/.env`):
```
HA_URL=http://192.168.0.148:8123
HA_TOKEN=<long-lived-access-token>
HA_SENSOR=binary_sensor.office_occupancy
SERVER_URL=http://192.168.0.148/pi2w-server
```

## Local Development

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate && pip install -e .

# Run server locally
./run.sh
# or: source .venv/bin/activate && python server.py

# Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/art/preview
```

## Hardware Configuration

- **Server**: devsrv (192.168.0.148), Ubuntu, Nginx reverse proxy
- **Home Assistant**: Docker on devsrv, port 8123, config at `~/homeassistant/config/`
- **Pi hostname**: pi2w.local (192.168.0.189)
- **Pi user**: piroot (SSH key auth, password disabled)
- **Display**: Inky Impression 7.3" Spectra, 800x480, 7-color
- **Display driver**: `inky.inky_e673` (use `from inky.auto import auto`)
- **Refresh interval**: 30 minutes (or on occupancy change via HA webhook)
- **Display refresh time**: ~30 seconds

## Key Implementation Details

- Images generated at 1792x1024 via DALL-E 3, resized to 800x480
- 7-color palette: black, white, red, yellow, green, blue, orange
- Floyd-Steinberg dithering for color quantization
- LLM-generated prompts (GPT-4o-mini) for vibrant, creative art
- LLM-generated quotes with random themes
- Adaptive text color based on background brightness
- Time-of-day prompts: morning (5-12), afternoon (12-17), evening (17-21), night (21-5)

## Project Structure

```
pi2w-server/
├── server.py              # Entry point (imports pi2w.app)
├── pi2w/                  # Main package
│   ├── app.py             # FastAPI application factory
│   ├── config.py          # Configuration dataclasses
│   ├── models.py          # Domain models
│   ├── adapters/          # External service adapters
│   ├── generators/        # Content generators (prompts, quotes)
│   ├── imaging/           # Image processing (quantizer, text renderer)
│   └── services/          # Business logic (ArtService)
├── pi_client/             # Raspberry Pi client
│   ├── display_client.py  # Fetches art and updates display
│   ├── webhook_listener.py # HTTP listener + scheduler (runs as service)
│   └── .env.example       # Template for Pi .env file
├── nginx-pi2w.conf        # Nginx config snippet
└── pi2w-server.service    # Systemd service file
```

## Environment Variables

Server requires `.env` file:
```
OPENAI_API_KEY=sk-...
```

Pi client requires `.env` file (see `pi_client/.env.example`).

## Home Assistant Configuration

HA config location: `~/homeassistant/config/` on devsrv

**rest_command** (in `configuration.yaml`):
```yaml
rest_command:
  pi2w_refresh:
    url: "http://192.168.0.189:8080/refresh"
    method: GET
```

**Automation** (in `automations.yaml`):
```yaml
- id: pi2w_display_on_occupancy
  alias: Pi2W Display - Refresh on office occupancy
  triggers:
  - platform: state
    entity_id: binary_sensor.office_occupancy
    to: "on"
  conditions:
  - condition: time
    after: "07:00:00"
    before: "23:59:59"
  actions:
  - action: rest_command.pi2w_refresh
  mode: single
```

After modifying HA config: `sudo docker restart homeassistant`

**HA Sensors** (in `configuration.yaml`):
```yaml
sensor:
  - platform: rest
    name: Pi2W Server
    resource: http://localhost/pi2w-server/status
    json_attributes:
      - last_generation
      - generation_count
    value_template: "{{ value_json.status }}"
    scan_interval: 60
  - platform: rest
    name: Pi2W Display
    resource: http://192.168.0.189:8080/status
    json_attributes:
      - service_uptime_seconds
      - quiet_hours
      - last_refresh
      - refresh_count
      - latest_image
    value_template: "{{ value_json.status }}"
    scan_interval: 60
```

## API Endpoints

### Server (http://192.168.0.148/pi2w-server)

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Simple health check, returns `{"status": "ok"}` |
| `GET /status` | Detailed status with last generation info (prompt, quote, artist, timestamp) |
| `GET /art` | Generate new art image (params: width, height, colors, style, prompt) |
| `GET /art/latest` | Return last generated image (cached in memory, lost on restart) |
| `GET /art/preview` | Preview prompt without generating image |
| `GET /tv` | Self-refreshing HTML page for TV/Chromecast display |

### Pi Client (http://pi2w.local:8080)

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Simple health check, returns `OK` |
| `GET /status` | Detailed status (uptime, quiet_hours, last_refresh, refresh_count, latest_image) |
| `GET /refresh` | Trigger display refresh (respects rate limit and quiet hours) |
| `GET /art/latest` | Return last displayed image (saved to `~/pi2w-client/latest.png`) |
