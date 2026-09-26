# Question:
# Build a simple calculator using if/elif/else.
# Take two numbers and an operator (+, -, *, /) from the user.
# Compute and print the result.
# Handle division by zero.
#
# Example:
#   Input: 10, +, 5  -> Output: 10 + 5 = 15
#   Input: 8, /, 2   -> Output: 8 / 2 = 4.0
#   Input: 5, /, 0   -> Output: Error: Cannot divide by zero

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print(f"Error: Unknown operator '{operator}'. Use +, -, *, /")
