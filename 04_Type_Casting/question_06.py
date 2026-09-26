# Question 6 (Medium):
# Convert the string '3.14' to a float.
# Use it in an arithmetic expression (compute the area of a circle with radius 5).
# Print the result.

# Solution:
pi_str = '3.14'
pi = float(pi_str)
print("pi as string:", pi_str, "| Type:", type(pi_str))
print("pi as float :", pi, "| Type:", type(pi))

radius = 5
area = pi * radius ** 2
print(f"Area of circle (radius={radius}): {area}")

# Output:
# pi as string: 3.14 | Type: <class 'str'>
# pi as float : 3.14 | Type: <class 'float'>
# Area of circle (radius=5): 78.5
