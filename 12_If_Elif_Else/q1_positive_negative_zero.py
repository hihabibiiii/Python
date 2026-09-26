# Question:
# Take a number from the user.
# Print 'Positive' if it is greater than 0,
# 'Negative' if it is less than 0,
# or 'Zero' if it equals 0.
#
# Example:
#   Input: 5   -> Output: Positive
#   Input: -3  -> Output: Negative
#   Input: 0   -> Output: Zero

number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
