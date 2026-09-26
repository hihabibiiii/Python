# Question:
# Take a string from the user.
# Check if the string starts with 'A' OR ends with 'n'.
# Use logical operators with string methods.

# Example:
# Enter a string: Adrian
# The string starts with 'A' or ends with 'n'.

text = input("Enter a string: ")

if text.startswith("A") or text.endswith("n"):
    print("The string starts with 'A' or ends with 'n' (or both).")
    if text.startswith("A"):
        print("  -> It starts with 'A'.")
    if text.endswith("n"):
        print("  -> It ends with 'n'.")
else:
    print("The string does NOT start with 'A' and does NOT end with 'n'.")
