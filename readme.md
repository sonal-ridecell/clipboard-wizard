# Clipboard Wizard

A macOS CLI application written in Python that monitors the clipboard and automatically replaces text based on predefined mappings.

## Features

- Continuously monitors the clipboard for changes
- Automatically replaces text based on predefined mappings
- Configurable replacement dictionary
- Simple and lightweight

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/clipboard_wizard.git
   cd clipboard_wizard
   ```

2. Make sure Python 3 is installed on your macOS system.

3. Make the scripts executable:
   ```
   chmod +x clipboard_wizard.py
   chmod +x start.sh
   ```

## Usage

### Starting the application

Run the application using the start script:
```
./start.sh
```

This will start the Clipboard Wizard in the background. The application will continuously monitor your clipboard and automatically replace text according to the mappings defined in the configuration file.

### Example

1. Copy text containing "omg" to your clipboard.
2. Clipboard Wizard will automatically replace "omg" with "oh my god!" in your clipboard.
3. When you paste, you'll see "oh my god!" instead of "omg".

### Stopping the application

To stop the application, use:
```
pkill -f clipboard_wizard.py
```

## Configuration

The application uses a configuration file (`config.json`) stored in the application directory. You can customize the mappings by editing this file:

```json
{
  "mappings": {
    "omg": "oh my god!",
    "brb": "be right back",
    "lol": "laughing out loud"
  },
  "check_interval": 0.5
}
```

- `mappings`: A dictionary of text to be replaced and their replacements
- `check_interval`: How often to check the clipboard (in seconds)

## Requirements

- macOS (uses `pbcopy` and `pbpaste` commands)
- Python 3.x