# Question: Write a program that asks the user to enter two numbers and divides them.
# Use try/except to catch ZeroDivisionError if the user enters 0 as the divisor.
# Print an appropriate error message if division by zero occurs.

# Example:
# Enter numerator: 10
# Enter denominator: 0
# Error: Cannot divide by zero!

# Enter numerator: 10
# Enter denominator: 2
# Result: 5.0

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
