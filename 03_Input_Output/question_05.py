# Question 5 (Easy):
# Use the `end` parameter of print() to print multiple items
# on the same line without automatic newlines between them.

# Solution:
print("One ", end="")
print("Two ", end="")
print("Three ", end="")
print("Four")

# Also demonstrate end with a custom character:
print("A", end="-")
print("B", end="-")
print("C")

# Output:
# One Two Three Four
# A-B-C
