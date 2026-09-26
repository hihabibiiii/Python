# Question 13 (Hard):
# Define a function called flatten that takes a nested list (list of lists)
# and returns a single flat list containing all the elements.

# Solution:
def flatten(nested_list):
    flat = []
    for item in nested_list:
        if type(item) == list:
            for element in item:
                flat.append(element)
        else:
            flat.append(item)
    return flat

# Test with examples
nested1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print("Nested:", nested1)
print("Flat:  ", flatten(nested1))

nested2 = [["a", "b"], ["c"], ["d", "e", "f"]]
print("\nNested:", nested2)
print("Flat:  ", flatten(nested2))

nested3 = [[10, 20], 30, [40, 50]]
print("\nMixed (flat items + sublists):", nested3)
print("Flat:", flatten(nested3))

# Example Output:
# Nested: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Flat:   [1, 2, 3, 4, 5, 6, 7, 8, 9]
