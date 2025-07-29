# Keylogger Project (Educational)

## Overview
This project demonstrates how a basic keylogger works using Python and `pynput`.
It records keystrokes locally, grouping them into readable words and sentences with timestamps.

**Disclaimer:**  
This keylogger is for **educational purposes only**. It should not be used for malicious purposes.

---

## Features
- Logs all keystrokes with timestamps.
- Groups characters into complete words and sentences.
- Formats special keys, such as:
  - `[SPACE]`
  - `[ENTER]`
  - `[BACKSPACE]`
  - `[TAB]`
  - `[SHIFT]`, `[CTRL]`, etc.
- Adds session headers:


=== Logging Started at YYYY-MM-DD HH:MM:SS ===


---

## Requirements
- Python 3.8+
- Install `pynput`:
```bash
pip install pynput

1. Run the keylogger: python keylogger.py
2. Type text in any window.
3. Press ESC to stop logging.
4. View the log: type key_log.txt

Example Output

=== Logging Started at 2025-07-24 22:25:01 ===
[2025-07-24 22:25:05] Typed: Hello World!

Future Improvements
- Add support for saving logs to a secure remote server.
- Add live console monitoring.
