import platform
import shutil
from datetime import timedelta
import os

from widgets.base_widget import Widget

class SystemInfoWidget(Widget):
    def display(self):
        print("\n--- System Information ---")
        print(f"Operating System: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.machine()}")
        print(f"Python Version: {platform.python_version()}")

        # Disk Usage
        try:
            total, used, free = shutil.disk_usage('/') # Assuming root partition
            print(f"Disk Usage: {used / (1024**3):.2f} GB used of {total / (1024**3):.2f} GB ({free / (1024**3):.2f} GB free)")
        except Exception as e:
            print(f"Could not retrieve disk usage: {e}")

        # Uptime (Linux specific, for cross-platform psutil would be better)
        if platform.system() == "Linux":
            try:
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    uptime_string = str(timedelta(seconds=uptime_seconds))
                    print(f"Uptime: {uptime_string}")
            except FileNotFoundError:
                print("Uptime: Not available (Linux /proc/uptime not found).")
            except Exception as e:
                print(f"Could not retrieve uptime: {e}")
        else:
            print("Uptime: Not available (requires psutil for non-Linux systems).")
