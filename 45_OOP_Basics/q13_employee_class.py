# Question: Create a class Employee with name, salary, department.
# Add method give_raise(percentage) that increases the salary.

# Example output:
# Employee: Alice
# Department: Engineering
# Salary: $5000
# After 10% raise: $5500.00
# After 15% raise: $6325.00

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_raise(self, percentage):
        increase = self.salary * (percentage / 100)
        self.salary += increase
        print(f"After {percentage}% raise: ${self.salary:.2f}")

    def display(self):
        print(f"Employee:   {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary:     ${self.salary:.2f}")

# Create employees
emp1 = Employee("Alice", 5000, "Engineering")
emp1.display()

print()
emp1.give_raise(10)
emp1.give_raise(15)

print()
emp2 = Employee("Bob", 4000, "Marketing")
emp2.display()
emp2.give_raise(20)
