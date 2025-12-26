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
└─────────────────────────┘         └─────────────────────────┘
                                             │
                                             ▼
                                   ┌─────────────────────────┐
                                   │  Inky Impression 7.3"   │
                                   │  800x480, 7-color       │
                                   │  E673 driver            │
                                   └─────────────────────────┘
```

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
**Service**: `pi2w-display.service` (refreshes every 30 minutes)

```bash
# Deploy client code
scp pi_client/display_client.py piroot@pi2w.local:~/pi2w-client/

# Service management
ssh piroot@pi2w.local "sudo systemctl restart pi2w-display"
ssh piroot@pi2w.local "sudo systemctl status pi2w-display"
ssh piroot@pi2w.local "journalctl -u pi2w-display -f"

# Manual run
ssh piroot@pi2w.local "python3 ~/pi2w-client/display_client.py --server http://192.168.0.148/pi2w-server"
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
- **Pi hostname**: pi2w.local
- **Pi user**: piroot (SSH key auth, password disabled)
- **Display**: Inky Impression 7.3" Spectra, 800x480, 7-color
- **Display driver**: `inky.inky_e673` (use `from inky.auto import auto`)
- **Refresh interval**: 30 minutes (via systemd service)
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
├── nginx-pi2w.conf        # Nginx config snippet
└── pi2w-server.service    # Systemd service file
```

## Environment Variables

Server requires `.env` file:
```
OPENAI_API_KEY=sk-...
```
