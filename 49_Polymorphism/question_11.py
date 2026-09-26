# Question:
# Create an Animal hierarchy with 5 different animals.
# Each makes a different sound via sound() method.
# Call sound() in a loop - polymorphism in action.

class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

class Sheep(Animal):
    def sound(self):
        return "Baa!"

class Duck(Animal):
    def sound(self):
        return "Quack!"

animals = [
    Dog("Rex"),
    Cat("Whiskers"),
    Cow("Bessie"),
    Sheep("Dolly"),
    Duck("Donald")
]

print("Animal Sounds:")
for animal in animals:
    print(f"  {animal.name} ({type(animal).__name__}): {animal.sound()}")
