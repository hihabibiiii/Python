# Question:
# Create a base class Vehicle with make and year.
# Create a child class Car that uses super().__init__() to call parent constructor.
# Car adds a doors attribute.

class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def info(self):
        return f"{self.year} {self.make}"

class Car(Vehicle):
    def __init__(self, make, year, doors):
        super().__init__(make, year)   # Call parent __init__
        self.doors = doors

    def info(self):
        return f"{super().info()} (Car, {self.doors} doors)"

v = Vehicle("Generic", 2020)
c = Car("Toyota", 2022, 4)

print(v.info())
print(c.info())
