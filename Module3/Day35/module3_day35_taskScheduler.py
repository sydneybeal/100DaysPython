"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module3_day35_taskScheduler.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

import subprocess
import sys
import time

python_path = "/Users/sbeal603/.virtualenvs/100DaysPython/bin/python"
subprocess.Popen([python_path, "greeting.py"])

sys_platform = sys.platform
print(sys_platform)

if sys_platform == "win32" or sys_platform == "cygwin":
    subprocess.Popen(["start", "../../Module2/Day19/declaration.txt"], shell=True)
elif sys_platform == "darwin":
    subprocess.Popen(["open", "../../Module2/Day19/declaration.txt"])
elif sys_platform == "linux":
    subprocess.Popen(["see", "../../Module2/Day19/declaration.txt"])
else:
    print(f"Unknown operating system: {sys_platform}")


try:
    sleep_time = float(input("How many minutes should the timer last?\n")) * 60
except TypeError:
    print(f"{sleep_time} is not a valid entry.")
    raise
except KeyboardInterrupt:
    print("The program was cancelled by the user.")
else:
    time.sleep(sleep_time)
    subprocess.Popen(["open", "alarm.mp3"])
finally:
    print("Goodbye")
