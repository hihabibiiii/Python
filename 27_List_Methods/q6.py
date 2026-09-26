# Question: Use index() to find the position of an element in a list.
# index(value) returns the index of the FIRST occurrence.
# Raises ValueError if the element is not found.
# Example:
#   List: ['cat', 'dog', 'bird', 'dog']
#   index('dog') -> 1

animals = ["cat", "dog", "bird", "dog", "fish"]
print("List:", animals)

position = animals.index("dog")
print(f"index('dog'): {position}  (first occurrence)")

# Handle element not present
try:
    pos = animals.index("lion")
except ValueError:
    print("ValueError: 'lion' is not in the list.")
