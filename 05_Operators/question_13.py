# Question 13 (Hard):
# Implement a simple calculator.
# Ask the user for two numbers and an operator (+, -, *, /).
# Perform the chosen operation and print the result.

# Solution:
num1 = float(input("Enter first number : "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

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
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Unknown operator. Please use +, -, *, or /")

# Example Input / Output:
# Enter first number : 15
# Enter operator (+, -, *, /): *
# Enter second number: 4
# 15.0 * 4.0 = 60.0
