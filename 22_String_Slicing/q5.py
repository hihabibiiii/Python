# Question: Extract the middle part of a string by leaving out the first and last 2 characters.
# Use slicing with [2:-2].
# Example:
#   Input: "Hello, World!"
#   Output: llo, World

text = input("Enter a string (at least 5 characters): ")
if len(text) < 5:
    print("String must have at least 5 characters.")
else:
    middle = text[2:-2]
    print("Middle part (excluding first and last 2):", middle)
