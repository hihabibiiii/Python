# Question: Rotate a list right by k positions using slicing.
# Right rotation: last k elements move to the front.
# Example:
#   List: [1, 2, 3, 4, 5], k=2
#   Rotated right by 2: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
k = int(input("Enter k (number of positions to rotate right): "))

k = k % len(numbers)  # Handle k > list length
rotated = numbers[-k:] + numbers[:-k]

print("Original list:", numbers)
print(f"Rotated right by {k}:", rotated)
