# Question:
# Create a class Car with __init__ taking multiple parameters:
# make, model, year, and color.
# Print the car details.

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

my_car = Car("Toyota", "Camry", 2022, "Blue")
print(my_car.display())

your_car = Car("Honda", "Civic", 2020, "Red")
print(your_car.display())
