# Question:
# Take a number from the user and compute its factorial using a for loop.
# Factorial of n (written n!) = 1 x 2 x 3 x ... x n
#
# Example:
#   Input: 5  -> Output: 5! = 120
#   Input: 6  -> Output: 6! = 720
#   Note: 0! = 1

number = int(input("Enter a non-negative integer to find its factorial: "))

factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print(f"{number}! = {factorial}")
