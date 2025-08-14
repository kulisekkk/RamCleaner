import subprocess
import time
from time import sleep
from plyer import notification
import ctypes
import keyboard
import sys

while True:
    try:
        notification.notify("RAM cleaner.", "Ram cleaned.", timeout=5)
        print("Clearing ram...")
        subprocess.run(["rammap.exe", "-Ew"])

        # Responsive 10-minute wait with Shift+F5 detection
        sleep_time = 600  # 10 minutes
        interval = 0.5    # check every 0.5 seconds
        for _ in range(int(sleep_time / interval)):
            if keyboard.is_pressed('shift+f5'):
                print("Shift+F5 detected. Exiting...")
                notification.notify("RAM cleaner.", "Exiting...", timeout=5)
                sys.exit()
            sleep(interval)

    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(
            0,
            "RamMap not found! Make sure RamMap is in the same folder as this EXE and its name is rammap.exe, exiting in 10 seconds.",
            "Error!",
            0x10
        )
        sleep(10)
        sys.exit()
    except OSError:
        ctypes.windll.user32.MessageBoxW(
            0,
            "You need to run this EXE with administrator privileges, rammap wont work without them. Exiting in 10 seconds.",
            "Error!",
            0x10
        )
        sleep(10)
        sys.exit()
