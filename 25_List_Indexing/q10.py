# Question: Handle IndexError gracefully when the user provides an invalid index.
# Use try/except to catch the error and display a helpful message.
# Example:
#   List: ['a', 'b', 'c']
#   Index: 10 -> Error: Index 10 is out of range. Valid range: 0 to 2.

items = ["alpha", "beta", "gamma", "delta", "epsilon"]
print("List:", items)
print(f"Valid index range: 0 to {len(items) - 1}")

user_input = input("Enter an index: ")
try:
    index = int(user_input)
    print(f"Element at index {index}: '{items[index]}'")
except IndexError:
    print(f"IndexError: Index {index} is out of range. Valid range: 0 to {len(items) - 1}.")
except ValueError:
    print("ValueError: Please enter a valid integer.")
