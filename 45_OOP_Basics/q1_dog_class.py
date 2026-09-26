# Question: Create a simple class Dog with an attribute 'name' and a method bark().
# Create a Dog object and call its bark() method.

# Example output:
# Dog's name: Buddy
# Buddy says: Woof! Woof!

class Dog:
    def __init__(self, name):
        self.name = name  # attribute

    def bark(self):       # method
        print(f"{self.name} says: Woof! Woof!")

# Create a Dog object
my_dog = Dog("Buddy")
print(f"Dog's name: {my_dog.name}")
my_dog.bark()

# Create another dog
another_dog = Dog("Max")
another_dog.bark()
