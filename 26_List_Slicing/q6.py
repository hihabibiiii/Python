# Question: Split a list into two halves using slicing.
# Use integer division to find the midpoint, then slice.
# Example:
#   List: [1, 2, 3, 4, 5, 6]  (mid = 3)
#   First half:  [1, 2, 3]
#   Second half: [4, 5, 6]

numbers = [1, 2, 3, 4, 5, 6]
print("Full list:", numbers)

mid = len(numbers) // 2
first_half = numbers[:mid]
second_half = numbers[mid:]

print("First half:", first_half)
print("Second half:", second_half)
