# Question: Modify object attributes after creation.
# Create an object, print it, change an attribute, then print again.

# Example output:
# Before modification:
#   Name: Alice, Age: 25
# 
# Modifying name to 'Alicia' and age to 26...
# 
# After modification:
#   Name: Alicia, Age: 26

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"  Name: {self.name}, Age: {self.age}")

# Create object
person = Person("Alice", 25)

print("Before modification:")
person.display()

# Modify attributes directly using dot notation
print("\nModifying name to 'Alicia' and age to 26...")
person.name = "Alicia"
person.age = 26

print("\nAfter modification:")
person.display()

# You can even add NEW attributes dynamically (not recommended but possible)
person.city = "London"
print(f"\nDynamically added city: {person.city}")
