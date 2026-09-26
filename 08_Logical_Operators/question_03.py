# Question:
# Take a number from the user and check if it is NOT zero.
# Use the `not` operator.

# Example:
# Enter a number: 5
# 5 is not zero.

num = int(input("Enter a number: "))

if not num == 0:
    print(f"{num} is not zero.")
else:
    print("The number is zero.")
