# Question:
# Create a class Student where __init__ validates input.
# If age is negative, raise a ValueError.
# If name is empty, raise a ValueError.

class Student:
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if age < 0:
            raise ValueError(f"Age cannot be negative. Got: {age}")
        self.name = name.strip()
        self.age = age

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age})"

# Valid student
s = Student("Alice", 20)
print(s)

# Invalid student - negative age
try:
    s2 = Student("Bob", -5)
except ValueError as e:
    print(f"Error: {e}")

# Invalid student - empty name
try:
    s3 = Student("", 22)
except ValueError as e:
    print(f"Error: {e}")
