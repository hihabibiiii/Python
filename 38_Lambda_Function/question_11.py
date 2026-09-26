# Question:
# Create a list of lambdas, one for each arithmetic operation:
# add, subtract, multiply, divide.
# Call each one with the same two numbers.

operations = [
    ("Add",      lambda a, b: a + b),
    ("Subtract", lambda a, b: a - b),
    ("Multiply", lambda a, b: a * b),
    ("Divide",   lambda a, b: a / b if b != 0 else "undefined"),
]

a, b = 10, 3
print(f"Operations on {a} and {b}:")
for name, op in operations:
    print(f"  {name}: {op(a, b)}")
