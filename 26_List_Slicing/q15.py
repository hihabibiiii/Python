# Question: Implement the merge step of merge sort using slicing.
# Given a list where the first half and second half are each sorted,
# merge them into a single sorted list.
# Example:
#   List: [1, 3, 5, 7, 2, 4, 6, 8]
#   Left:  [1, 3, 5, 7]  (first half, sorted)
#   Right: [2, 4, 6, 8]  (second half, sorted)
#   Merged: [1, 2, 3, 4, 5, 6, 7, 8]

numbers = [1, 3, 5, 7, 2, 4, 6, 8]
mid = len(numbers) // 2

left = numbers[:mid]
right = numbers[mid:]

print("Original list:", numbers)
print("Left half:", left)
print("Right half:", right)

# Merge two sorted halves
merged = []
i = 0
j = 0

while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        merged.append(left[i])
        i += 1
    else:
        merged.append(right[j])
        j += 1

# Append remaining elements
merged = merged + left[i:] + right[j:]

print("Merged sorted list:", merged)
