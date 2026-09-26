# Question 9 (Medium):
# Take the length and width of a rectangle from the user.
# Compute and print the area (length * width) and perimeter (2 * (length + width)).

# Solution:
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width : "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area      = {length} * {width} = {area}")
print(f"Perimeter = 2 * ({length} + {width}) = {perimeter}")

# Example:
# Enter rectangle length: 8
# Enter rectangle width : 5
# Area      = 8.0 * 5.0 = 40.0
# Perimeter = 2 * (8.0 + 5.0) = 26.0
