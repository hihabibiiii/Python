# Question:
# Create a Vehicle base class.
# Create Car and Bike as child classes with their own specific attributes.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} travels at {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def describe(self):
        return f"Car: {self.brand}, {self.num_doors} doors, {self.speed} km/h"

class Bike(Vehicle):
    def __init__(self, brand, speed, is_electric):
        super().__init__(brand, speed)
        self.is_electric = is_electric

    def describe(self):
        kind = "Electric" if self.is_electric else "Regular"
        return f"{kind} Bike: {self.brand}, {self.speed} km/h"

car = Car("Toyota", 180, 4)
bike = Bike("Trek", 30, True)

print(car.describe())
print(bike.describe())
