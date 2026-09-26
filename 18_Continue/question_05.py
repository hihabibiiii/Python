# Question:
# A list contains some None values.
# Loop through the list and skip None values using `continue`.
# Print only the non-None values.

# Example:
# List: [1, None, 3, None, 5, 6, None, 8]
# Valid values: 1 3 5 6 8

data = [1, None, 3, None, 5, 6, None, 8]
print(f"Original list: {data}")
print("Valid values: ", end="")

for item in data:
    if item is None:
        continue
    print(item, end=" ")
print()
