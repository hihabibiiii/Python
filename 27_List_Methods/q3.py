# Question: Use insert() to add an item at a specific position in the list.
# insert(index, item) inserts 'item' BEFORE the element at 'index'.
# Example:
#   Before: ['a', 'b', 'd', 'e']
#   insert(2, 'c')
#   After:  ['a', 'b', 'c', 'd', 'e']

letters = ["a", "b", "d", "e"]
print("Original list:", letters)

letters.insert(2, "c")   # Insert 'c' at index 2
print("After insert(2, 'c'):", letters)

# Insert at the beginning
letters.insert(0, "Z")
print("After insert(0, 'Z'):", letters)
