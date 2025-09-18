#!/usr/bin/env python3
"""
Clipboard Wizard - A clipboard monitoring utility for macOS.

This script continuously monitors the clipboard for changes and replaces text
based on predefined mappings.
"""

import time
import json
import sys
from pathlib import Path
import subprocess

# Configuration file path
CONFIG_FILE = Path(__file__).parent / "config.json"
DEFAULT_CONFIG = {
    "mappings": {
        "omg": "oh my god!",
    },
    "check_interval": 0.5  # seconds
}


def load_config():
    """Load configuration from file or create default if not exists."""
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        else:
            # Write default config
            with open(CONFIG_FILE, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=2)
            return DEFAULT_CONFIG
    except Exception as e:
        print(f"Error loading configuration: {e}", file=sys.stderr)
        return DEFAULT_CONFIG


def get_clipboard_content():
    """Get the current clipboard content using pbpaste."""
    try:
        result = subprocess.run(['pbpaste'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error reading clipboard: {e}", file=sys.stderr)
        return ""


def set_clipboard_content(text):
    """Set the clipboard content using pbcopy."""
    try:
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(text.encode())
        return True
    except Exception as e:
        print(f"Error setting clipboard: {e}", file=sys.stderr)
        return False


def process_clipboard(text, mappings):
    """Process clipboard content and apply text replacements."""
    modified = text
    for source, target in mappings.items():
        modified = modified.replace(source, target)
    return modified


def main():
    """Main function to monitor clipboard and replace text."""
    config = load_config()
    mappings = config.get("mappings", {})
    interval = config.get("check_interval", 0.5)

    print("Clipboard Wizard is running. Press Ctrl+C to exit.")

    previous_content = ""

    try:
        while True:
            current_content = get_clipboard_content()

            # If clipboard content changed and not empty
            if current_content != previous_content and current_content:
                # Process the clipboard content
                modified_content = process_clipboard(current_content, mappings)

                # Only update clipboard if the content was actually modified
                if modified_content != current_content:
                    set_clipboard_content(modified_content)
                    previous_content = modified_content
                    print(f"Replaced: {current_content} -> {modified_content}")
                else:
                    previous_content = current_content

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nClipboard Wizard stopped.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()