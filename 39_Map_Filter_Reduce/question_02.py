# Question:
# Use map() to convert a list of numeric strings to integers.

# Example:
# Input:  ['1', '2', '3', '4', '5']
# Output: [1, 2, 3, 4, 5]

str_numbers = ["10", "25", "3", "47", "8"]
print(f"Original (strings): {str_numbers}")

int_numbers = list(map(int, str_numbers))
print(f"Converted (ints):   {int_numbers}")
print(f"Sum: {sum(int_numbers)}")
