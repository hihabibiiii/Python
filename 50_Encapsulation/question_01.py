# Question:
# Create a class Person with a private attribute __name.
# Show that it cannot be accessed directly from outside the class.

class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute (name mangling)

    def get_name(self):
        return self.__name

p = Person("Alice")

# Access via method
print(f"Name (via method): {p.get_name()}")

# Direct access fails
try:
    print(p.__name)  # This will raise AttributeError
except AttributeError as e:
    print(f"Direct access failed: {e}")

# Name mangling - can be accessed as _ClassName__attr (not recommended)
print(f"Via mangled name: {p._Person__name}  (not recommended!)")
