# Question: Try to open a file that may not exist.
# Ask the user to enter a filename. Try to open and read it.
# Use try/except to catch FileNotFoundError and print a helpful message.

# Example:
# Enter filename to open: ghost_file.txt
# Error: The file 'ghost_file.txt' was not found!
# Tip: Make sure the file exists in the current directory.

# Enter filename to open: notes.txt
# File contents:
# (prints file content here)

filename = input("Enter filename to open: ")

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("File contents:")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found!")
    print("Tip: Make sure the file exists in the current directory.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
