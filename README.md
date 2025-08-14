# RAM Cleaner Script

A simple Python script that periodically frees up RAM using **RAMMap** and sends desktop notifications. Useful for systems with limited memory or high RAM usage.

## Features

- Clears RAM every 10 minutes (configurable).
- Sends desktop notifications when RAM is cleared.
- Handles missing RAMMap or insufficient permissions gracefully with error popups.

## Requirements

- Python 3.6+
- [RAMMap](https://docs.microsoft.com/en-us/sysinternals/downloads/rammap) (must be in the same folder as the script)
- Python packages:
  - `plyer` (for notifications)

Install dependencies via pip:

```bash
pip install plyer
