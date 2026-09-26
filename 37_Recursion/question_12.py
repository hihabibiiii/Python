# Question:
# Write a recursive function to flatten a nested list.
# flatten([1, [2, 3], [4, [5, 6]]]) = [1, 2, 3, 4, 5, 6]

# Example Output:
# Original: [1, [2, 3], [4, [5, 6]], 7]
# Flattened: [1, 2, 3, 4, 5, 6, 7]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Original:  {nested}")
print(f"Flattened: {flatten(nested)}")
