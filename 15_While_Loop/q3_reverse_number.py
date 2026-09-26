# Question:
# Take a number from the user and reverse its digits using a while loop.
#
# Example:
#   Input: 12345  -> Output: 54321
#   Input: 1000   -> Output: 1  (leading zeros are dropped)

number = int(input("Enter a positive integer: "))
original = number

reversed_number = 0
while number > 0:
    digit = number % 10           # Get the last digit
    reversed_number = reversed_number * 10 + digit
    number = number // 10         # Remove the last digit

print(f"Reversed number of {original} = {reversed_number}")
