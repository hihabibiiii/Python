# Question:
# Create a class Box where __init__ takes width and height.
# The constructor also computes and stores the area and perimeter automatically.

class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height          # Computed in constructor
        self.perimeter = 2 * (width + height)  # Computed in constructor

    def __str__(self):
        return (f"Box(width={self.width}, height={self.height}, "
                f"area={self.area}, perimeter={self.perimeter})")

b1 = Box(5, 3)
b2 = Box(10, 7)
print(b1)
print(b2)
