# Question 6 (Medium):
# Take a number from the user.
# Check if it is between 1 and 100 (inclusive) using comparison operators.
# Print whether it is in range or out of range.

# Solution:
number = int(input("Enter a number: "))

if number >= 1 and number <= 100:
    print(f"{number} is within the range [1, 100].")
else:
    print(f"{number} is OUT of the range [1, 100].")

# Example:
# 50 -> within range
# 0  -> out of range
# 101 -> out of range
