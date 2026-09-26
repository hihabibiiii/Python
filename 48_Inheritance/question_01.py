# Question:
# Create a base class Animal with a name attribute and a speak() method.
# Create a derived class Dog that inherits from Animal and adds a bark() method.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def bark(self):
        return f"{self.name} says: Woof! Woof!"

# Create Dog object (it inherits from Animal)
d = Dog("Buddy")
print(d.speak())  # Inherited method
print(d.bark())   # Dog-specific method
print(f"Is Dog an Animal? {isinstance(d, Animal)}")
