# Question:
# Demonstrate Python's name mangling.
# Private attributes __attr become _ClassName__attr.

class MyClass:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected (convention)"
        self.__private = "I am private (name mangled)"

    def show(self):
        print(f"Inside class: {self.__private}")

obj = MyClass()

# Public - direct access works
print(obj.public)

# Protected - works but discouraged
print(obj._protected)

# Private - direct access fails
try:
    print(obj.__private)
except AttributeError as e:
    print(f"Error: {e}")

# Via name mangling
print(obj._MyClass__private)  # Works but not recommended

# Via method (correct way)
obj.show()
