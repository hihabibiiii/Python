# Question 5 (Easy):
# Use the popitem() method to remove and return the last inserted key-value pair.
# Demonstrate this by calling popitem() multiple times.

# Solution:
data = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4
}

print("Original dictionary:", data)
print()

# Pop items one by one
for i in range(3):
    removed = data.popitem()
    print(f"Removed: {removed}  |  Remaining: {data}")

print("\nFinal dictionary:", data)

# Example Output:
# Original dictionary: {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
#
# Removed: ('fourth', 4)  |  Remaining: {'first': 1, 'second': 2, 'third': 3}
# Removed: ('third', 3)   |  Remaining: {'first': 1, 'second': 2}
# Removed: ('second', 2)  |  Remaining: {'first': 1}
#
# Final dictionary: {'first': 1}
