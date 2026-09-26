# Question:
# Create a tuple of 5 numbers.
# Convert it to a list, modify the list (add an element, change one),
# then convert back to a tuple.

# Example Output:
# Original tuple: (1, 2, 3, 4, 5)
# Modified list: [1, 2, 99, 4, 5, 6]
# New tuple: (1, 2, 99, 4, 5, 6)

original = (1, 2, 3, 4, 5)
print(f"Original tuple: {original}")

temp_list = list(original)
temp_list[2] = 99     # Modify element
temp_list.append(6)   # Add element
print(f"Modified list: {temp_list}")

new_tuple = tuple(temp_list)
print(f"New tuple: {new_tuple}")
