# RAM Cleaner Script

A simple Python script, executable that periodically frees up RAM using **RAMMap** and sends desktop notifications. Useful for systems with limited memory or high RAM usage.

## Features

- Clears RAM every 15 minutes.
- Sends desktop notifications when RAM is cleared.
- Handles missing RAMMap or insufficient permissions gracefully with error popups.

## SHA256 (for advanced users)
the built version's SHA256 is as follows:
d942c2ffacf2e1acfdc643b758bc5fb3d201617b4ca6c91aee7a67ece0eedbb4

To verify:
1. Open PowerShell or Command Prompt.
2. Run:
   ```powershell
   Get-FileHash "path\to\ram_cleaner.exe" -Algorithm SHA256

## Requirements

- Python 3.0+ at least
- [RAMMap](https://docs.microsoft.com/en-us/sysinternals/downloads/rammap) (must be in the same folder as the script)
- Python packages:
  - `plyer` (for notifications)
  - `time` (for pauses between cleans)
  - `subprocess` (to actually run the rammap file)
  - `ctypes` (for error pop ups)
  - `sys` (For application exit)
  - `webbrowser` (To open a website to download RamMap)

Install dependencies via pip:
for linux:
```bash
python3 pip install -r requirements.txt
```
for windows:
```batch
python3 -m pip install -r requirements.txt
```

