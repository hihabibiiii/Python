# Question: Delete a slice of a list using the `del` statement.
# `del list[start:end]` removes elements in the specified range.
# Example:
#   Before: [10, 20, 30, 40, 50, 60]
#   del numbers[2:5]
#   After:  [10, 20, 60]

numbers = [10, 20, 30, 40, 50, 60]
print("Original list:", numbers)

del numbers[2:5]   # Deletes elements at indices 2, 3, 4
print("After del numbers[2:5]:", numbers)
