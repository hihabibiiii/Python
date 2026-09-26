# Question: Reverse a list using slicing [::-1].
# A step of -1 traverses the list backwards without modifying the original.
# Example:
#   Original: [1, 2, 3, 4, 5]
#   Reversed: [5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
reversed_list = numbers[::-1]
print("Reversed list (slicing):", reversed_list)
print("Original list unchanged:", numbers)
