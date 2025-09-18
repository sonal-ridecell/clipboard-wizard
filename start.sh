#!/bin/bash

# Make the Python script executable
chmod +x clipboard_wizard.py

# Start the clipboard wizard in the background
./clipboard_wizard.py &

echo "Clipboard Wizard started in the background."
echo "To see the output, use: ps aux | grep clipboard_wizard"
echo "To stop it, use: pkill -f clipboard_wizard.py"