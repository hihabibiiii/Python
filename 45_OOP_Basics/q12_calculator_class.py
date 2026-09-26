# Question: Create a class Calculator with methods add, subtract, multiply, divide.

# Example output:
# === Calculator ===
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0
# 10 / 0 = Error: Cannot divide by zero!

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulo(self, a, b):
        if b == 0:
            return "Error: Cannot mod by zero!"
        return a % b

# Create and use the calculator
calc = Calculator()
print("=" * 25)
print("       Calculator")
print("=" * 25)

a, b = 10, 5
print(f"{a} + {b} = {calc.add(a, b)}")
print(f"{a} - {b} = {calc.subtract(a, b)}")
print(f"{a} * {b} = {calc.multiply(a, b)}")
print(f"{a} / {b} = {calc.divide(a, b)}")
print(f"{a} / 0 = {calc.divide(a, 0)}")
print(f"{a} ^ {b} = {calc.power(a, b)}")
print(f"{a} % 3 = {calc.modulo(a, 3)}")
