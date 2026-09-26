# Question:
# Use isinstance() and issubclass() to check inheritance relationships.

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(f"isinstance(dog, Dog):    {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, Cat):    {isinstance(dog, Cat)}")
print(f"isinstance(cat, Animal): {isinstance(cat, Animal)}")

print(f"\nissubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")
print(f"issubclass(Dog, Cat):    {issubclass(Dog, Cat)}")
print(f"issubclass(Animal, Dog): {issubclass(Animal, Dog)}")
