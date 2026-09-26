# Question: Create a class Car with attributes make, model, and year.
# Create a car object, set its attributes, and print them.

# Example output:
# Car Details:
# Make:  Toyota
# Model: Camry
# Year:  2022
# Full:  2022 Toyota Camry

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print("Car Details:")
        print(f"  Make:  {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year:  {self.year}")
        print(f"  Full:  {self.year} {self.make} {self.model}")

# Create car objects
car1 = Car("Toyota", "Camry", 2022)
car1.display()

print()
car2 = Car("Ford", "Mustang", 2023)
car2.display()
