# Question: Use 'from math import' to import specific functions directly.
# Import sqrt, pi, pow, and factorial individually, and use them without the 'math.' prefix.

# Example output:
# Using 'from math import' — no need for 'math.' prefix!
# Pi = 3.141592653589793
# sqrt(144) = 12.0
# pow(2, 10) = 1024.0
# factorial(6) = 720

from math import sqrt, pi, pow, factorial

print("Using 'from math import' — no need for 'math.' prefix!")
print(f"Pi = {pi}")
print(f"sqrt(144) = {sqrt(144)}")
print(f"pow(2, 10) = {pow(2, 10)}")
print(f"factorial(6) = {factorial(6)}")

# User input
number = int(input("\nEnter a number to compute its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"factorial({number}) = {factorial(number)}")
