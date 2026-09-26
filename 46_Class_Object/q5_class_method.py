# Question: Add a method to a class and call it via the object.
# Demonstrate that methods are functions that belong to a class.

# Example output:
# Calculator object created.
# Result of add: 15
# Result of square: 25
# Saying hello: Hello from Calculator!

class Calculator:
    def __init__(self, label="My Calculator"):
        self.label = label

    # Methods are functions that belong to the class
    def add(self, a, b):
        return a + b

    def square(self, n):
        return n * n

    def say_hello(self):
        print(f"Hello from {self.label}!")

# Create a Calculator object
calc = Calculator("Super Calculator")
print(f"Calculator object created: '{calc.label}'")

# Call methods via the object using dot notation
result1 = calc.add(10, 5)
print(f"Result of add(10, 5): {result1}")

result2 = calc.square(5)
print(f"Result of square(5): {result2}")

calc.say_hello()
