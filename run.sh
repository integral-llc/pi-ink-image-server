#!/bin/bash
# Run the Pi2W Content Server

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check for .env file
if [ ! -f .env ]; then
    echo "Error: .env file not found"
    echo "Copy .env.example to .env and add your OpenAI API key"
    exit 1
fi

# Check for virtual environment
if [ ! -d .venv ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .
else
    source .venv/bin/activate
fi

# Run server
echo "Starting Pi2W Content Server on http://0.0.0.0:8000"
python server.py
