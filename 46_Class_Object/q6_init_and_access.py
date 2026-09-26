# Question: Create a class with __init__ and access its attributes via the object.
# Show how __init__ (constructor) initializes the object's state.

# Example output:
# Creating a Laptop object...
# __init__ called! Setting up the laptop.
# 
# Laptop Details:
# Brand:  Dell
# RAM:    16 GB
# Price:  $999.99

class Laptop:
    def __init__(self, brand, ram_gb, price):
        print("__init__ called! Setting up the laptop.")
        self.brand = brand      # instance attribute set by __init__
        self.ram_gb = ram_gb    # instance attribute set by __init__
        self.price = price      # instance attribute set by __init__

    def display(self):
        print("\nLaptop Details:")
        print(f"  Brand:  {self.brand}")
        print(f"  RAM:    {self.ram_gb} GB")
        print(f"  Price:  ${self.price}")

print("Creating a Laptop object...")
laptop1 = Laptop("Dell", 16, 999.99)
laptop1.display()

# Accessing attributes via the object
print(f"\nDirect access: laptop1.brand = {laptop1.brand}")
print(f"Direct access: laptop1.ram_gb = {laptop1.ram_gb}")
