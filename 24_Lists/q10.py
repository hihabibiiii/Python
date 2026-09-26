# Question: Remove duplicates from a list using a new list and `not in` check.
# Iterate through the original list; add each item to the new list only if it's not already there.
# Example:
#   Original: [1, 2, 3, 2, 4, 3, 5, 1]
#   Unique:   [1, 2, 3, 4, 5]

original = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4]
print("Original list:", original)

unique = []
for item in original:
    if item not in unique:
        unique.append(item)

print("List with duplicates removed:", unique)
