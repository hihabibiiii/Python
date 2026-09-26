# Question: Rotate a list left by one position.
# Moving left means the first element goes to the end.
# Example:
#   Original: [1, 2, 3, 4, 5]
#   Rotated left by 1: [2, 3, 4, 5, 1]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# Remove the first element and append it to the end
first_element = numbers[0]
rotated = numbers[1:] + [first_element]

print("Rotated left by 1:", rotated)
