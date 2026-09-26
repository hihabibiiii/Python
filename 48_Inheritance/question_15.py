# Question:
# Create an Employee hierarchy:
# Employee (base) -> Manager, Engineer, Intern
# Each computes salary differently.

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def compute_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{type(self).__name__}: {self.name} | Salary: ${self.compute_salary():,.2f}"

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_pct):
        super().__init__(name, base_salary)
        self.bonus_pct = bonus_pct  # % bonus

    def compute_salary(self):
        return self.base_salary * (1 + self.bonus_pct / 100)

class Engineer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate=50):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def compute_salary(self):
        return self.base_salary + (self.overtime_hours * self.hourly_rate)

class Intern(Employee):
    def __init__(self, name, base_salary, stipend=500):
        super().__init__(name, base_salary)
        self.stipend = stipend

    def compute_salary(self):
        return self.base_salary + self.stipend

employees = [
    Manager("Alice", 80000, 20),
    Engineer("Bob", 70000, 15),
    Intern("Charlie", 20000),
    Employee("Diana", 50000),
]

print("Employee Salary Report")
print("=" * 45)
for emp in employees:
    print(emp)
