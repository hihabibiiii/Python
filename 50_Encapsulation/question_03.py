# Question:
# Use a setter method to modify a private attribute with validation.
# The setter ensures the value is valid before accepting it.

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)  # Use setter for validation

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0 or age > 150:
            raise ValueError(f"Age {age} is not valid. Must be 0-150.")
        self.__age = age

s = Student("Alice", 20)
print(f"Name: {s.get_name()}, Age: {s.get_age()}")

# Valid update
s.set_age(21)
print(f"After update: Age = {s.get_age()}")

# Invalid update
try:
    s.set_age(-5)
except ValueError as e:
    print(f"Error: {e}")
