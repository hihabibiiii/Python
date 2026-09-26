# Question: Compare two objects of the same class with different data.
# By default, == compares identity (same object in memory), not data.
# Show this default behavior.

# Example output:
# p1: Alice, 25
# p2: Bob, 30
# p3: Alice, 25  (same data as p1, but different object)
# 
# p1 == p2 → False (different data)
# p1 == p3 → False (same data but different object in memory!)
# p1 is p3 → False (different memory locations)
# p1 == p1 → True  (same object)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, {self.age}"

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p3 = Person("Alice", 25)  # Same data as p1, but different object!

print(f"p1: {p1.info()}")
print(f"p2: {p2.info()}")
print(f"p3: {p3.info()} (same data as p1, but different object)")

print(f"\nDefault == comparison (checks identity):")
print(f"p1 == p2 → {p1 == p2}  (different data and different object)")
print(f"p1 == p3 → {p1 == p3}  (same data but different object — still False!)")
print(f"p1 is p3 → {p1 is p3}  (different memory locations)")
print(f"p1 == p1 → {p1 == p1}  (same object)")
print(f"p1 is p1 → {p1 is p1}  (same memory location)")

print("\nNote: To compare by data, override __eq__ method (see q9 in Polymorphism topic)")
