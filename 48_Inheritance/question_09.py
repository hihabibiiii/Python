# Question:
# Override __str__ in a child class to customize how it prints.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        # Override __str__ from parent
        return f"Student(id={self.student_id}, name='{self.name}', age={self.age})"

p = Person("Alice", 30)
s = Student("Bob", 20, "S1042")

print(p)   # Uses Person.__str__
print(s)   # Uses Student.__str__ (overridden)
