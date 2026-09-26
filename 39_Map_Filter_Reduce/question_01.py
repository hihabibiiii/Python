# Question:
# Use map() to convert a list of strings to uppercase.

# Example:
# Input:  ['hello', 'world', 'python']
# Output: ['HELLO', 'WORLD', 'PYTHON']

words = ["hello", "world", "python", "programming"]
print(f"Original: {words}")

uppercased = list(map(str.upper, words))
print(f"Uppercased: {uppercased}")
