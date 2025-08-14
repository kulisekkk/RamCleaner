# RAM Cleaner Script

A simple Python script that periodically frees up RAM using **RAMMap** and sends desktop notifications. Useful for systems with limited memory or high RAM usage.

## Features

- Clears RAM every 10 minutes.
- Sends desktop notifications when RAM is cleared.
- Handles missing RAMMap or insufficient permissions gracefully with error popups.

## Requirements

- Python 3.6+
- [RAMMap](https://docs.microsoft.com/en-us/sysinternals/downloads/rammap) (must be in the same folder as the script)
- Python packages:
  - `plyer` (for notifications)
  - `time` (for pauses between cleans)
  - `subprocess` (to actually run the rammap file)
  - `ctypes` (for error pop ups)
  - `sys` (For application exit)

Install dependencies via pip:
for linux:
```bash
python3 pip install -r requirements.txt
```
for windows:
```batch
python3 -m pip install -r requirements.txt
```
