# Question:
# Demonstrate duck typing in Python.
# Two unrelated classes both have a make_sound() method.
# Call them the same way regardless of the class type.

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Car:
    def make_sound(self):
        return "Vroom!"

# Polymorphic behavior - same call, different behavior
objects = [Dog(), Cat(), Car()]
for obj in objects:
    print(f"{type(obj).__name__}: {obj.make_sound()}")
