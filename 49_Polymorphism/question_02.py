# Question:
# Method overriding: Parent class has a speak() method.
# Child classes override it with their own version.

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

animals = [Animal(), Dog(), Cat(), Duck()]
for animal in animals:
    print(f"{type(animal).__name__}.speak() -> {animal.speak()}")
