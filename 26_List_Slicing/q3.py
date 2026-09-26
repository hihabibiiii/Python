# Question: Slice every other element from a list (step=2).
# Use [::2] to pick elements at indices 0, 2, 4, ...
# Example:
#   List: [1, 2, 3, 4, 5, 6, 7, 8]
#   Output: [1, 3, 5, 7]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Full list:", numbers)
every_other = numbers[::2]
print("Every other element (step=2):", every_other)
