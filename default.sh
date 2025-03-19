#!/bin/bash

# Define paths
TOOL_NAME="ScanItUp"
INSTALL_DIR="/opt/$TOOL_NAME"
EXECUTABLE="/usr/local/bin/scanitup"
SCRIPT_NAME="scanner.py"

# Move the tool to /opt/ if it's not already there
if [ ! -d "$INSTALL_DIR" ]; then
    echo "[*] Moving $TOOL_NAME to $INSTALL_DIR..."
    sudo mv ~/"$TOOL_NAME" "$INSTALL_DIR"
else
    echo "[*] $TOOL_NAME already exists in $INSTALL_DIR, skipping move."
fi

# Create a global wrapper script
echo "[*] Creating global command..."
echo '#!/bin/bash' | sudo tee "$EXECUTABLE" > /dev/null
echo "cd $INSTALL_DIR && python3 $SCRIPT_NAME \"\$@\"" | sudo tee -a "$EXECUTABLE" > /dev/null

# Make the wrapper script executable
echo "[*] Setting permissions..."
sudo chmod +x "$EXECUTABLE"

# Done!
echo "[+] Installation complete! You can now run 'scanitup' from anywhere."
    
    This script is designed to be run from the same directory as the tool's source code. It will move the tool to  /opt/ScanItUp , create a global command called  scanitup , and make the command executable. 
    To run the script, save it to a file called  default.sh  in the same directory as the tool's source code. Then, run the following command: 
    chmod +x default.sh