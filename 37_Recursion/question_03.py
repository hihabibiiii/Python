# Question:
# Write a recursive function to compute factorial of a number.
# factorial(n) = n * factorial(n-1), base case: factorial(0) = 1

# Example:
# Enter N: 6
# 6! = 720

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter N: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{n}! = {factorial(n)}")
