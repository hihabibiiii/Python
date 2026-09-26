# Question 11 (Hard):
# Define a function called factorial that takes a non-negative integer n
# and returns n! (n factorial).
# n! = n * (n-1) * (n-2) * ... * 1, and 0! = 1

# Solution:
def factorial(n):
    if n < 0:
        return None  # factorial undefined for negatives
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test with examples
for n in range(0, 11):
    print(f"{n}! = {factorial(n)}")

# Get input from user
n = int(input("\nEnter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"{n}! = {factorial(n)}")

# Example Input:  7
# Example Output: 7! = 5040
