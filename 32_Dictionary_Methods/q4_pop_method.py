# Question 4 (Easy):
# Use the pop() method to remove a key from a dictionary and capture its value.
# Demonstrate that pop() returns the removed value.
# Also show what happens when you pop with a default (key doesn't exist).

# Solution:
inventory = {
    "apples": 10,
    "bananas": 5,
    "cherries": 20,
    "dates": 8
}
print("Before pop():", inventory)

# Remove 'bananas' and get its value
removed_value = inventory.pop("bananas")
print(f"\nRemoved key 'bananas', its value was: {removed_value}")
print("After pop():", inventory)

# Pop a key that doesn't exist — use default to avoid KeyError
result = inventory.pop("mango", "Key not found")
print(f"\nTrying to pop 'mango': {result}")
print("Dictionary unchanged:", inventory)

# Example Output:
# Before pop(): {'apples': 10, 'bananas': 5, 'cherries': 20, 'dates': 8}
# Removed key 'bananas', its value was: 5
# After pop(): {'apples': 10, 'cherries': 20, 'dates': 8}
# Trying to pop 'mango': Key not found
