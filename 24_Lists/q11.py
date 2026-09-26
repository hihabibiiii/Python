# Question: Flatten a nested list [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6] using loops.
# Iterate through the outer list, then iterate through each inner list.
# Example:
#   Input:  [[1, 2], [3, 4], [5, 6]]
#   Output: [1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested)

flat = []
for inner_list in nested:
    for item in inner_list:
        flat.append(item)

print("Flattened list:", flat)
