# Question: Slice the last 4 characters of a string.
# Use negative indexing in slicing with [-4:].
# Example:
#   Input: "Hello, World!"
#   Output: rld!

text = input("Enter a string (at least 4 characters): ")
last_four = text[-4:]
print("Last 4 characters:", last_four)
