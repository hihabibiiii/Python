# Question: Add a class variable (shared by all instances) and an instance variable (unique per object).
# Show the difference between them.

# Example output:
# Class variable (shared): school = 'Python Academy'
# dog1.name = 'Buddy' (instance variable, unique to dog1)
# dog2.name = 'Max'   (instance variable, unique to dog2)
# 
# Dog.total_dogs = 2 (class variable, counts all dogs created)

class Dog:
    # CLASS variable — shared by ALL instances of Dog
    species = "Canis lupus familiaris"
    total_dogs = 0  # Tracks how many Dog objects have been created

    def __init__(self, name, breed):
        # INSTANCE variables — unique to each Dog object
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1  # Increment the class variable

    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}")
        print(f"Species (shared): {self.species}")

# Create dog objects
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Max", "Poodle")
d3 = Dog("Bella", "Beagle")

print("=== Instance Variables (unique per object) ===")
d1.display()
print()
d2.display()

print("\n=== Class Variable (shared by all) ===")
print(f"Dog.total_dogs = {Dog.total_dogs}  (class variable)")
print(f"d1.total_dogs  = {d1.total_dogs}   (accessed via instance, same value)")
print(f"d2.total_dogs  = {d2.total_dogs}   (accessed via instance, same value)")

# Modifying instance name doesn't affect others
d1.name = "Buddy (updated)"
print(f"\nAfter updating d1.name: d1={d1.name}, d2={d2.name}")
