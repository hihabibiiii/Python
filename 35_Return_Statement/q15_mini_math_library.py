# Question 15 (Hard):
# Build a mini math library with functions: add, subtract, multiply, divide.
# Each returns its result. Then create a calculate() function that calls
# the appropriate operation based on the operator symbol (+, -, *, /).

# Solution:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # division by zero guard
    return a / b

def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return None  # unknown operator

# Demo
print("Mini Math Library")
print("=" * 30)
expressions = [(10, "+", 5), (10, "-", 5), (10, "*", 5), (10, "/", 5), (10, "/", 0)]
for a, op, b in expressions:
    result = calculate(a, op, b)
    if result is None:
        print(f"{a} {op} {b} = Error")
    else:
        print(f"{a} {op} {b} = {result}")

# Interactive calculator
print("\n--- Interactive Calculator ---")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: "))

result = calculate(a, op, b)
if result is None:
    print("Error: Invalid operator or division by zero.")
else:
    print(f"Result: {a} {op} {b} = {result}")
