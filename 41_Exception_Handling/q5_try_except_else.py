# Question: Demonstrate the try/except/else block.
# Ask the user for two numbers and divide them.
# The 'else' block should run ONLY if no exception occurred.
# Print a success message in the else block.

# Example:
# Enter numerator: 20
# Enter denominator: 4
# Division successful!
# Result: 5.0

# Enter numerator: 20
# Enter denominator: 0
# Error: Division by zero is not allowed!
# (else block does NOT run)

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Please enter valid numbers!")
else:
    # This block runs ONLY if no exception was raised
    print("Division successful!")
    print(f"Result: {result}")
