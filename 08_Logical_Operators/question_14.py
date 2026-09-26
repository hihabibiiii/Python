# Question:
# Take a number from the user and check if it is a 3-digit number.
# A 3-digit number must be >= 100 AND <= 999.
# Use `and` operator.

# Example:
# Enter a number: 456
# 456 is a 3-digit number.

num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print(f"{num} is a 3-digit number.")
else:
    print(f"{num} is NOT a 3-digit number.")
