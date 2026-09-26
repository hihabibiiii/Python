# Question 11 (Hard):
# Take a 3-digit number from the user.
# Use arithmetic operators (// and %) ONLY to extract:
#   - Hundreds digit
#   - Tens digit
#   - Ones digit
# Print each digit.

# Solution:
number = int(input("Enter a 3-digit number: "))

hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10

print(f"Number: {number}")
print(f"Hundreds digit: {hundreds}")
print(f"Tens digit    : {tens}")
print(f"Ones digit    : {ones}")

# Example:
# Enter a 3-digit number: 376
# Number: 376
# Hundreds digit: 3
# Tens digit    : 7
# Ones digit    : 6
