# Question: Add a __str__ method to a class so the object prints nicely.
# Without __str__, printing an object shows something like <__main__.Dog object at 0x...>.
# With __str__, it prints a readable description.

# Example output:
# Without __str__: <__main__.BasicDog object at 0x...>
# With __str__: Dog: Rex (Labrador, 3 years old)

class BasicDog:
    """No __str__ method defined."""
    def __init__(self, name):
        self.name = name

class Dog:
    """Has a __str__ method for readable output."""
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        # This is called when you print(object) or str(object)
        return f"Dog: {self.name} ({self.breed}, {self.age} years old)"

    def __repr__(self):
        # repr() is for developers — shows how to recreate the object
        return f"Dog(name='{self.name}', breed='{self.breed}', age={self.age})"

# Without __str__
basic = BasicDog("Max")
print(f"Without __str__: {basic}")  # Shows memory address

# With __str__
dog = Dog("Rex", "Labrador", 3)
print(f"With __str__: {dog}")       # Shows our custom string

# str() vs repr()
print(f"\nstr(dog):  {str(dog)}")
print(f"repr(dog): {repr(dog)}")
