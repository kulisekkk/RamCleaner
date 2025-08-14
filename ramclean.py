import subprocess
import time
from time import sleep
from plyer import notification
import ctypes
import sys

while True:
    try:
        notification.notify("RAM clearer.", "Ram cleaned.", timeout=5)
        print("Clearing ram...")
        subprocess.run(["RAMMap64.exe", "-Ew"])
        sleep(600)
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, "RamMap not found! make sure RamMap is in the same folder as this EXE. Exiting in 10 seconds.", "Error!", 0x10)
        sleep(10)
        sys.exit()
    except OSError:
        ctypes.windll.user32.MessageBoxW(0, "You need to run this EXE as admin! exiting in 10 seconds.", "Error!", 0x10)
        sleep(10)
        sys.exit()
