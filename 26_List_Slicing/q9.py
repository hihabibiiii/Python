# Question: Replace a slice of a list with new values using slice assignment.
# Slice assignment lets you replace a section of a list with new values.
# Example:
#   Before: [1, 2, 3, 4, 5]
#   Replace indices 1:4 with [20, 30]
#   After:  [1, 20, 30, 5]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers[1:4] = [20, 30]   # Replaces indices 1, 2, 3 with 20, 30
print("After slice assignment (numbers[1:4] = [20, 30]):", numbers)
