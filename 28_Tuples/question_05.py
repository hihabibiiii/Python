# Question:
# Create a tuple of 5 fruits.
# Ask the user to enter a fruit name.
# Check if it is in the tuple using `in` and print the result.

# Example:
# Fruits: ('apple', 'banana', 'cherry', 'date', 'elderberry')
# Enter a fruit: cherry
# cherry is in the tuple!

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"Fruits: {fruits}")

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print(f"{fruit} is in the tuple!")
else:
    print(f"{fruit} is NOT in the tuple.")
