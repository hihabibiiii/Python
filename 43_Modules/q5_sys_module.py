# Question: Import the sys module and print the Python version and other system info.

# Example output:
# === SYS Module Demo ===
# Python Version: 3.11.4 (main, Jul  5 2023, ...)
# Python Version (short): 3.11.4
# Platform: win32
# Executable: C:\Python311\python.exe
# Default Encoding: utf-8

import sys

print("=" * 35)
print("       SYS Module Demo")
print("=" * 35)

print(f"Python Version (full): {sys.version}")
print(f"Python Version Info: {sys.version_info}")
print(f"Python Major.Minor: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Platform: {sys.platform}")
print(f"Python Executable Path: {sys.executable}")
print(f"Default String Encoding: {sys.getdefaultencoding()}")
print(f"Maximum Integer Size: {sys.maxsize}")
