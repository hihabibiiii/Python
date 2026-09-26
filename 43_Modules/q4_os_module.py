# Question: Import the os module and print the current working directory.
# Also list some useful os module features.

# Example output:
# === OS Module Demo ===
# Current Working Directory: C:\Users\Habibullah\OneDrive\Desktop\...
# Path Separator on this OS: \
# Line separator on this OS: \r\n  (or \n on Linux/Mac)
# CPU Count: 8

import os

print("=" * 30)
print("      OS Module Demo")
print("=" * 30)

# Print current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# Other useful os info
print(f"Path Separator on this OS: {os.sep}")
print(f"Current platform: {os.name}")

# List files in current directory
print(f"\nFiles/folders in current directory:")
items = os.listdir('.')
for i, item in enumerate(items[:10], 1):  # Show first 10
    print(f"  {i}. {item}")

if len(items) > 10:
    print(f"  ... and {len(items) - 10} more items.")
