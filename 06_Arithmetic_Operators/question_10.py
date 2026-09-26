# Question 10 (Medium):
# Take two sides of a right triangle from the user.
# Compute the hypotenuse using the Pythagorean theorem: c = (a**2 + b**2) ** 0.5
# Print the result.

# Solution:
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

hypotenuse = (a ** 2 + b ** 2) ** 0.5

print(f"Hypotenuse = sqrt({a}^2 + {b}^2) = sqrt({a**2 + b**2}) = {hypotenuse:.4f}")

# Example:
# Enter side a: 3
# Enter side b: 4
# Hypotenuse = sqrt(3.0^2 + 4.0^2) = sqrt(25.0) = 5.0000
