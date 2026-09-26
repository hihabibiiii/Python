# Question:
# Child class adds NEW attributes and methods not in the parent.
# Parent: Employee with name and salary.
# Child: Manager with department and manages() method.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department   # New attribute
        self.team = []                 # New attribute

    def add_team_member(self, member):  # New method
        self.team.append(member)

    def details(self):
        base = super().details()
        return f"{base}, Department: {self.department}, Team size: {len(self.team)}"

mgr = Manager("Alice", 85000, "Engineering")
mgr.add_team_member("Bob")
mgr.add_team_member("Charlie")
mgr.add_team_member("Diana")

print(mgr.details())
print(f"Team: {mgr.team}")
