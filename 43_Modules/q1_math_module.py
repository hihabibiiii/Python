# Question: Import the math module and use math.pi to print the value of pi,
# and math.sqrt() to compute the square root of a number entered by the user.

# Example output:
# Value of pi: 3.141592653589793
# Enter a number: 25
# Square root of 25.0 = 5.0

import math

print(f"Value of pi: {math.pi}")

number = float(input("Enter a number: "))
result = math.sqrt(number)
print(f"Square root of {number} = {result}")
