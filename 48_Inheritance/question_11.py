# Question:
# Multiple inheritance: class C inherits from both class A and class B.
# Demonstrate that C has access to methods from both parents.

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):  # Multiple inheritance
    def __init__(self, name):
        self.name = name

    def quack(self):
        return f"{self.name} says: Quack!"

d = Duck("Donald")
print(d.quack())  # Own method
print(d.fly())    # From Flyable
print(d.swim())   # From Swimmable

print(f"\nMRO: {[c.__name__ for c in Duck.__mro__]}")
