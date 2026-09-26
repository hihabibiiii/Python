# Question:
# Search for a name in a list.
# Use break when the name is found.
# Print the position (index) where the name was found.

# Example Output:
# Searching for: Charlie
# Found 'Charlie' at index 2!

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
search = input("Enter name to search: ").strip()

found = False
for i in range(len(names)):
    if names[i] == search:
        print(f"Found '{search}' at index {i}!")
        found = True
        break

if not found:
    print(f"'{search}' not found in the list.")
