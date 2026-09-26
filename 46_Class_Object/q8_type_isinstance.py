# Question: Use type() and isinstance() with class objects.
# Demonstrate how to check an object's type and whether it's an instance of a class.

# Example output:
# type(dog1) → <class '__main__.Dog'>
# type(cat1) → <class '__main__.Cat'>
# isinstance(dog1, Dog) → True
# isinstance(dog1, Cat) → False
# isinstance(dog1, Animal) → True  (because Dog is a subclass)

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog1 = Dog("Rex")
cat1 = Cat("Whiskers")
num = 42

print("=== type() checks ===")
print(f"type(dog1) → {type(dog1)}")
print(f"type(cat1) → {type(cat1)}")
print(f"type(num)  → {type(num)}")

print("\n=== isinstance() checks ===")
print(f"isinstance(dog1, Dog)    → {isinstance(dog1, Dog)}")
print(f"isinstance(dog1, Cat)    → {isinstance(dog1, Cat)}")
print(f"isinstance(dog1, Animal) → {isinstance(dog1, Animal)}")  # True! Dog inherits Animal
print(f"isinstance(cat1, Animal) → {isinstance(cat1, Animal)}")
print(f"isinstance(num, int)     → {isinstance(num, int)}")
print(f"isinstance(num, Dog)     → {isinstance(num, Dog)}")

print("\n=== type() vs isinstance() ===")
print("type() gives exact class; isinstance() also checks parent classes")
