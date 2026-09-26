# Question: Given a list, create a new list containing only the elements at even indices (0, 2, 4, ...).
# Use a loop with range() to select every even index.
# Example:
#   Input:  [10, 20, 30, 40, 50, 60]
#   Output: [10, 30, 50]

numbers = [10, 20, 30, 40, 50, 60]
print("Original list:", numbers)

even_index_elements = []
for i in range(0, len(numbers), 2):
    even_index_elements.append(numbers[i])

print("Elements at even indices:", even_index_elements)
