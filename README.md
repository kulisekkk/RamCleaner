# RAM Cleaner Script

A simple Python script (also available as an executable) that periodically frees up RAM using **RAMMap** and sends desktop notifications. Useful for systems with limited memory or high RAM usage.  

## Features
- Clears RAM every 15 minutes.  
- Sends desktop notifications when RAM is cleared.  
- Handles missing RAMMap or insufficient permissions gracefully with error popups.  

## Download the Executable
The pre-built `.exe` version is available in the [**Releases**](https://github.com/kulisekkk/RamCleaner/releases/tag/Cleaner) section of this repository.  

**SHA256** (for advanced users)  
The built version's SHA256 hash is:  

d942c2ffacf2e1acfdc643b758bc5fb3d201617b4ca6c91aee7a67ece0eedbb4

To verify:  
1. Open PowerShell or Command Prompt.  
2. Run:  
```powershell
Get-FileHash "path\to\ram_cleaner.exe" -Algorithm SHA256
```
## Requirements

- **Python 3.0+**  
- [**RAMMap**](https://docs.microsoft.com/en-us/sysinternals/downloads/rammap) (must be in the same folder as the script)  
- Python packages:
  - `plyer` (for notifications)  
  - `time` (for pauses between cleans)  
  - `subprocess` (to run the RAMMap executable)  
  - `ctypes` (for error popups)  
  - `sys` (for application exit)  
  - `webbrowser` (to open the RAMMap download page)

### Install Dependencies

For Linux:
```bash
python3 -m pip install -r requirements.txt
```
For Windows:
```batch
python3 -m pip install -r requirements.txt
```
