# Question:
# Demonstrate Method Resolution Order (MRO).
# Create a diamond inheritance pattern and print the MRO.

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):  # Multiple inheritance - diamond
    pass

d = D()
print(f"D inherits from B and C, both inherit from A.")
print(f"D().greet() -> '{d.greet()}'  (MRO determines which greet() is called)")
print(f"\nMRO of D: {[cls.__name__ for cls in D.__mro__]}")
print("Python follows C3 linearization for MRO.")
