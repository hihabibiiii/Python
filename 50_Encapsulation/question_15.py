# Question:
# Create a fully encapsulated Person class.
# Private: __name, __age, __email.
# Full validation in setters.
# __str__ method for display.

import re

class Person:
    def __init__(self, name, age, email):
        self.name = name    # Uses setter
        self.age = age      # Uses setter
        self.email = email  # Uses setter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = value.strip().title()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if not (0 <= value <= 150):
            raise ValueError(f"Age {value} is out of valid range (0-150).")
        self.__age = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        pattern = r"^[\w.+-]+@[\w-]+\.[\w.]+$"
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email format: {value}")
        self.__email = value.lower()

    def __str__(self):
        return f"Person(name='{self.__name}', age={self.__age}, email='{self.__email}')"

    def __repr__(self):
        return f"Person(name={self.__name!r}, age={self.__age!r}, email={self.__email!r})"

# Valid person
p = Person("alice smith", 25, "Alice@Example.COM")
print(p)

# Update via setters
p.age = 26
p.email = "alice.smith@company.org"
print(p)

# Validation tests
print()
for test in [
    ("", 25, "a@b.com"),
    ("Bob", -5, "b@c.com"),
    ("Charlie", 30, "not-an-email"),
]:
    try:
        bad = Person(*test)
    except (ValueError, TypeError) as e:
        print(f"Rejected {test}: {e}")
