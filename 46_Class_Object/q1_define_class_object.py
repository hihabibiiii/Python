# Question: Define a simple class and create an object (instance) from it.
# Show what a class is and how to create an object from it.

# Example output:
# Created a Person object!
# Name: Alice
# Type of object: <class '__main__.Person'>

class Person:
    """A simple Person class."""
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I am {self.name}!")

# Create an object (instance) from the class
person1 = Person("Alice")

print("Created a Person object!")
print(f"Name: {person1.name}")
print(f"Type of object: {type(person1)}")
person1.greet()

# 'person1' is an instance of the 'Person' class
print(f"\nIs person1 an instance of Person? {isinstance(person1, Person)}")
