# Question: Extract only the digits from the mixed string 'abc123def' using slicing
#           at known (hardcoded) positions.
# The digits '123' are at indices 3, 4, 5 -> slice [3:6].
# Example:
#   String: "abc123def"
#   Output: 123

mixed = "abc123def"
print("Original string:", mixed)
digits = mixed[3:6]
print("Extracted digits:", digits)
