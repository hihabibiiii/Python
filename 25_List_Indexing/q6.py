# Question: Swap the first and last elements of a list using indexing.
# Example:
#   Before: [1, 2, 3, 4, 5]
#   After:  [5, 2, 3, 4, 1]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# Swap first (index 0) and last (index -1)
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("After swapping first and last:", numbers)
