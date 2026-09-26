# Question:
# Create a class where the setter validates the type of input.
# If wrong type, raise TypeError.

class UserProfile:
    def __init__(self, username, age):
        self.username = username  # Public
        self.__age = None
        self.age = age  # Uses setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Age must be int, got {type(value).__name__}")
        if value < 0 or value > 150:
            raise ValueError(f"Age {value} out of valid range.")
        self.__age = value

u = UserProfile("alice99", 25)
print(f"{u.username}: age = {u.age}")

# Type error
try:
    u.age = "twenty"
except TypeError as e:
    print(f"TypeError: {e}")

# Value error
try:
    u.age = -1
except ValueError as e:
    print(f"ValueError: {e}")
