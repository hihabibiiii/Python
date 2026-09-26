# Question:
# Take a number from the user and check if it is between 1 and 100 (inclusive).
# Use the `and` operator.

# Example:
# Enter a number: 55
# 55 is between 1 and 100.

num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print(f"{num} is between 1 and 100.")
else:
    print(f"{num} is NOT between 1 and 100.")
