# Question: Extract every 3rd element from a list using slicing with step=3.
# Example:
#   List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#   Every 3rd element: [1, 4, 7, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Full list:", numbers)

every_third = numbers[::3]
print("Every 3rd element (step=3):", every_third)
