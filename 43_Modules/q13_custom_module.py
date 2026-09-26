# Question: Understand how to create your own module.
# In real Python, you would put helper functions in a separate file (e.g., mymath.py)
# and import them. Since we're demonstrating in one file, the module code and usage
# are both shown here with comments explaining the concept.

# =====================================================
# CONCEPT: A module is just a .py file with functions.
# Normally you would create TWO files:
# 
# File 1: mymath.py  (the module)
# ------------------------------------------
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# def is_even(n):
#     return n % 2 == 0
#
# PI = 3.14159
# ------------------------------------------
#
# File 2: main.py (your script that uses it)
# ------------------------------------------
# import mymath
#
# result = mymath.add(3, 4)
# print(result)          # 7
#
# print(mymath.PI)       # 3.14159
# ------------------------------------------
# =====================================================

# Since we're in one file, let's simulate the module using a class namespace:
print("=== Custom Module Demo ===\n")

# Simulating what 'mymath' module would contain
class mymath:
    """Simulated module: in real usage, this would be a separate .py file."""
    PI = 3.14159

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def circle_area(radius):
        return mymath.PI * radius ** 2

# Usage (as if we had 'import mymath')
print(f"mymath.PI = {mymath.PI}")
print(f"mymath.add(10, 5) = {mymath.add(10, 5)}")
print(f"mymath.multiply(4, 7) = {mymath.multiply(4, 7)}")
print(f"mymath.is_even(8) = {mymath.is_even(8)}")
print(f"mymath.circle_area(5) = {mymath.circle_area(5):.2f}")

print("\nTip: Create 'mymath.py' with these functions,")
print("then in another file use: import mymath")
