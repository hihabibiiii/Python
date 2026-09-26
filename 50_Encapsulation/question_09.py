# Question:
# Demonstrate protected attribute (_attribute) convention.
# It's accessible but signals "do not use from outside."

class Animal:
    def __init__(self, name, speed):
        self.name = name          # Public
        self._speed = speed       # Protected (convention - should not modify directly)
        self.__id = id(self)      # Private

    def run(self):
        return f"{self.name} runs at {self._speed} km/h"

class Cheetah(Animal):
    def __init__(self):
        super().__init__("Cheetah", 120)

    def sprint(self):
        # Child classes CAN access _protected attributes
        return f"Sprint speed: {self._speed} km/h!"

a = Animal("Lion", 80)
c = Cheetah()

print(a.run())
print(c.sprint())

# Can be accessed directly (but shouldn't be in good code)
print(f"Direct access to _speed (discouraged): {a._speed}")
print("Convention: _ prefix means 'internal use only'.")
