# Question:
# Create a tuple of fruits.
# Ask the user to enter a fruit.
# Use index() to find its position. Handle ValueError if not found.

# Example:
# Fruits: ('apple', 'banana', 'cherry', 'date')
# Enter a fruit: cherry
# 'cherry' is at index 2.

fruits = ("apple", "banana", "cherry", "date")
print(f"Fruits: {fruits}")

fruit = input("Enter a fruit to find: ").strip().lower()

try:
    idx = fruits.index(fruit)
    print(f"'{fruit}' is at index {idx}.")
except ValueError:
    print(f"'{fruit}' is not in the tuple.")
