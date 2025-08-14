import subprocess
import time
from time import sleep
from plyer import notification
import ctypes
import keyboard
import sys
import webbrowser

ctypes.windll.user32.MessageBoxW(0, "You are now running the ram cleaner. This program cleans your memory every 15 minutes. You can press SHIFT + F5 at any time to quit the program. Thank you for using this tool i made in my free time :)", "Ram cleaner by kulisekkk", 0x40)

while True:
    try:
        subprocess.run(["rammap.exe", "-Ew"])
        notification.notify("RAM cleaner.", "Ram cleaned. next cleanup is in 15 minutes..", timeout=5)

        # Responsive 15-minute wait with Shift+F5 detection
        sleep_time = 900  # 15 minutes
        interval = 0.1  # check every 0.1 seconds
        for _ in range(int(sleep_time / interval)):
            if keyboard.is_pressed('shift+f5'):
                print("Shift+F5 detected. Exiting...")
                notification.notify("RAM cleaner.", "Exiting...", timeout=5)
                sys.exit()
            sleep(interval)

    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(
            0,
            "RamMap not found! Make sure RamMap is in the same folder as this EXE and its name is rammap.exe, click OK to open a browser with the RAMMap download if you haven't downloaded it yet. It's necessary for this program to work, as it provides the core functionality.",
            "Error!",
            0x10
        )
        webbrowser.open("https://docs.microsoft.com/en-us/sysinternals/downloads/rammap")
        sys.exit()
    except OSError as e:
        if "elevation" in str(e).lower():
            ctypes.windll.user32.MessageBoxW(
                0,
                "You need to run this EXE with administrator privileges... RamMap needs Administator privileges due to its access to system memory.",
                "Error!",
                0x10
            )
        else:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"An unexpected OS error occurred:\n{e}",
                "Error!",
                0x10
            )
        sys.exit()
