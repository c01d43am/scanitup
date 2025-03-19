#!/bin/bash

# Define variables
TOOL_NAME="ScanItUp"
INSTALL_DIR="/opt/$TOOL_NAME"
EXECUTABLE="/usr/local/bin/scanitup"
SCRIPT_NAME="scanitup.py"

# Check if ScanItUp already exists in /opt/
if [ ! -d "$INSTALL_DIR" ]; then
    echo "[*] Moving $TOOL_NAME to $INSTALL_DIR..."
    sudo mv ~/scanitup "$INSTALL_DIR"
else
    echo "[*] $TOOL_NAME already exists in $INSTALL_DIR, skipping move."
fi

# Verify if the move was successful
if [ ! -d "$INSTALL_DIR" ]; then
    echo "[!] Failed to move $TOOL_NAME to $INSTALL_DIR. Exiting..."
    exit 1
fi

# Create the wrapper script
echo "[*] Creating global command..."
sudo bash -c "echo '#!/bin/bash' > $EXECUTABLE"
sudo bash -c "echo 'cd $INSTALL_DIR && python3 $SCRIPT_NAME \"\$@\"' >> $EXECUTABLE"

# Set permissions
echo "[*] Setting permissions..."
sudo chmod +x "$EXECUTABLE"

# Verify installation
if [ -x "$EXECUTABLE" ]; then
    echo "[✔] Installation complete! You can now run 'scanitup' from anywhere."
else
    echo "[!] Installation failed. Check permissions."
fi
