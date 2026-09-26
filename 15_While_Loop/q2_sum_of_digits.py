# Question:
# Take a number from the user and compute the sum of its digits using a while loop.
#
# Example:
#   Input: 1234  -> Output: Sum of digits = 10  (1+2+3+4)
#   Input: 999   -> Output: Sum of digits = 27  (9+9+9)

number = int(input("Enter a positive integer: "))
original = number

digit_sum = 0
while number > 0:
    digit = number % 10       # Get the last digit
    digit_sum = digit_sum + digit
    number = number // 10     # Remove the last digit

print(f"Sum of digits of {original} = {digit_sum}")
