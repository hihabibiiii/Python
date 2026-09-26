# Question:
# Create a class Person with a __init__ method that takes one parameter: name.
# Store it as an instance attribute and print a greeting when the object is created.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

p = Person("Alice")
print(p.greet())
print(f"Name attribute: {p.name}")
