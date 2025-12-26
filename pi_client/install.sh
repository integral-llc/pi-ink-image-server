#!/bin/bash
# Install Pi2W Display Client

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing Pi2W Display Client..."

# Install Python dependencies
pip3 install --break-system-packages -r "$SCRIPT_DIR/requirements.txt"

# Create systemd service
sudo tee /etc/systemd/system/pi2w-display.service > /dev/null << EOF
[Unit]
Description=Pi2W Display Client
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$SCRIPT_DIR
ExecStart=/usr/bin/python3 $SCRIPT_DIR/display_client.py --server http://SERVER_IP:8000 --interval 60
Restart=on-failure
RestartSec=30

[Install]
WantedBy=multi-user.target
EOF

echo ""
echo "Installation complete!"
echo ""
echo "Next steps:"
echo "1. Edit the service file to set your server IP:"
echo "   sudo nano /etc/systemd/system/pi2w-display.service"
echo ""
echo "2. Enable and start the service:"
echo "   sudo systemctl daemon-reload"
echo "   sudo systemctl enable pi2w-display"
echo "   sudo systemctl start pi2w-display"
echo ""
echo "Or run manually:"
echo "   python3 display_client.py --server http://YOUR_SERVER_IP:8000"
