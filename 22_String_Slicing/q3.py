# Question: Slice every other character from a string using step=2.
# Use slicing with [::2] to pick characters at indices 0, 2, 4, ...
# Example:
#   Input: "Python"
#   Output: Pto

text = input("Enter a string: ")
every_other = text[::2]
print("Every other character (step=2):", every_other)
