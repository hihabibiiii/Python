# Question: Use os.path to check if a file exists, get its size, and other path info.
# Ask the user for a filename and check if it exists in the current directory.

# Example output:
# Enter a filename to check: output.txt
# File 'output.txt' EXISTS!
# Full path: C:\Users\...\output.txt
# File size: 13 bytes
# Is a file: True
# Is a directory: False

import os

# Check a hardcoded file first (create one to test with)
test_file = 'os_path_test.txt'
with open(test_file, 'w') as f:
    f.write("This file is for testing os.path functions!")

print("=" * 40)
print("       os.path Module Demo")
print("=" * 40)

filename = input("Enter a filename to check: ").strip()

# Check existence
exists = os.path.exists(filename)
print(f"\nFile '{filename}' {'EXISTS' if exists else 'does NOT exist'}!")

if exists:
    print(f"Full path: {os.path.abspath(filename)}")
    print(f"File size: {os.path.getsize(filename)} bytes")
    print(f"Is a file: {os.path.isfile(filename)}")
    print(f"Is a directory: {os.path.isdir(filename)}")
    
    # Split path components
    dirname, basename = os.path.split(os.path.abspath(filename))
    name, ext = os.path.splitext(basename)
    print(f"Directory: {dirname}")
    print(f"Base name: {basename}")
    print(f"File name (no ext): {name}")
    print(f"Extension: {ext}")
else:
    print("Tip: Try entering 'os_path_test.txt' — it was just created!")
