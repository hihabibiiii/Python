# Question: Demonstrate that objects are independent — modifying one doesn't affect another.
# This is a key concept: each object has its own copy of instance attributes.

# Example output:
# Before modification:
#   dog1: Rex, 3 years old
#   dog2: Max, 5 years old
# 
# Modifying dog1's age to 4...
# 
# After modification:
#   dog1: Rex, 4 years old  ← changed
#   dog2: Max, 5 years old  ← UNCHANGED

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, {self.age} years old"

# Create two independent objects
dog1 = Dog("Rex", 3)
dog2 = Dog("Max", 5)

print("Before modification:")
print(f"  dog1: {dog1.info()}")
print(f"  dog2: {dog2.info()}")

# Modify ONLY dog1
print("\nModifying dog1's age to 4...")
dog1.age = 4

print("\nAfter modification:")
print(f"  dog1: {dog1.info()}  ← changed")
print(f"  dog2: {dog2.info()}  ← UNCHANGED (independent)")

print("\nKey point: Each object has its OWN copy of instance attributes.")
print(f"dog1 and dog2 are at different memory addresses: {id(dog1) != id(dog2)}")
