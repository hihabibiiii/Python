# Question:
# Multi-level inheritance: Animal -> Mammal -> Dog
# Each class adds attributes and methods.

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} breathes."

class Mammal(Animal):
    def __init__(self, name, warm_blooded=True):
        super().__init__(name)
        self.warm_blooded = warm_blooded

    def feed_young(self):
        return f"{self.name} feeds its young with milk."

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return f"{self.name} ({self.breed}) barks: Woof!"

dog = Dog("Rex", "German Shepherd")
print(dog.breathe())      # From Animal
print(dog.feed_young())   # From Mammal
print(dog.bark())         # From Dog

print(f"\nInheritance chain: {[c.__name__ for c in type(dog).__mro__]}")
