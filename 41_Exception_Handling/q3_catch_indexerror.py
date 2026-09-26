# Question: Create a list of 5 fruits. Ask the user to enter an index number.
# Try to access the list at that index. Use try/except to catch IndexError
# if the index is out of range, and print a helpful message.

# Example:
# Fruits: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Enter an index (0-4): 10
# Error: Index 10 is out of range! List has 5 items (valid indexes: 0 to 4).

# Enter an index (0-4): 2
# Fruit at index 2: cherry

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Fruits: {fruits}")

try:
    index = int(input("Enter an index (0-4): "))
    fruit = fruits[index]
    print(f"Fruit at index {index}: {fruit}")
except IndexError:
    print(f"Error: Index {index} is out of range! List has {len(fruits)} items (valid indexes: 0 to {len(fruits)-1}).")
except ValueError:
    print("Error: Please enter a valid integer index.")
