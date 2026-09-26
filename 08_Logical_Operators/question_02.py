# Question:
# Take a number from the user and check if it is either negative OR zero.
# Use the `or` operator.

# Example:
# Enter a number: -5
# -5 is negative or zero.

num = int(input("Enter a number: "))

if num < 0 or num == 0:
    print(f"{num} is negative or zero.")
else:
    print(f"{num} is a positive number.")
