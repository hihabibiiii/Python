# Question 12 (Hard):
# Take the radius of a circle from the user.
# Compute the area using the formula: area = 3.14159 * radius^2
# Print the result formatted to 4 decimal places.

# Solution:
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = pi * radius ** 2
print(f"Area of circle with radius {radius} = {area:.4f}")

# Example Input / Output:
# Enter the radius of the circle: 5
# Area of circle with radius 5.0 = 78.5398
