# Question:
# Call the parent class method from the child class using super().
# Both parent and child have a greet() method; child extends it.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}."

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def greet(self):
        # Call parent greet() and add more info
        parent_greeting = super().greet()
        return f"{parent_greeting} I work at {self.company}."

p = Person("Alice")
e = Employee("Bob", "TechCorp")

print(p.greet())
print(e.greet())
