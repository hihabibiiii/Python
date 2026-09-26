# Question: Create multiple objects from the same class.
# Each object has its own data but shares the same blueprint.

# Example output:
# Object 1: Toyota Corolla (2020)
# Object 2: Honda Civic (2022)
# Object 3: BMW 3-Series (2023)
# All are Car objects: True

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.brand} {self.model} ({self.year})"

# Create multiple objects from the SAME class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)
car3 = Car("BMW", "3-Series", 2023)

print(f"Object 1: {car1.info()}")
print(f"Object 2: {car2.info()}")
print(f"Object 3: {car3.info()}")

# All are instances of the same Car class
all_cars = isinstance(car1, Car) and isinstance(car2, Car) and isinstance(car3, Car)
print(f"All are Car objects: {all_cars}")

# Each object is independent — separate memory
print(f"\nAre car1 and car2 the same object? {car1 is car2}")
