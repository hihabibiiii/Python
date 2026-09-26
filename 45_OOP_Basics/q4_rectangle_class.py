# Question: Create a class Rectangle with width and height attributes.
# Add methods area() and perimeter(). Ask the user for dimensions.

# Example output:
# Enter width: 5
# Enter height: 3
# Rectangle: 5 x 3
# Area:      15 sq units
# Perimeter: 16 units
# Is it a square? No

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

width = float(input("Enter width: "))
height = float(input("Enter height: "))

rect = Rectangle(width, height)

print(f"\nRectangle: {rect.width} x {rect.height}")
print(f"Area:      {rect.area()} sq units")
print(f"Perimeter: {rect.perimeter()} units")
print(f"Is it a square? {'Yes' if rect.is_square() else 'No'}")
