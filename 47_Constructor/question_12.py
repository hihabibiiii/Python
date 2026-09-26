# Question:
# Create a class Profile where __init__ uses **kwargs for flexible attributes.
# Print all provided attributes.

class Profile:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self._fields = list(kwargs.keys())

    def display(self):
        print("Profile:")
        for field in self._fields:
            print(f"  {field}: {getattr(self, field)}")

# Create profiles with different fields
p1 = Profile(name="Alice", age=25, city="London")
p1.display()

print()
p2 = Profile(username="bob99", email="bob@example.com", role="admin")
p2.display()
