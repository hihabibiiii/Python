# Question:
# Take a number from the user and check if it is both positive AND even.
# Print an appropriate message.

# Example:
# Enter a number: 4
# 4 is positive and even.

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print(f"{num} is positive and even.")
else:
    print(f"{num} is NOT both positive and even.")
