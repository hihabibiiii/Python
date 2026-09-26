# Question 3 (Easy):
# Define a function called rectangle_area that takes length and width
# as parameters and returns the area of a rectangle.
# Call it with a few examples and print the results.

# Solution:
def rectangle_area(length, width):
    area = length * width
    return area

# Test with fixed values
print("Area of 5 x 3 rectangle:", rectangle_area(5, 3))
print("Area of 10 x 4 rectangle:", rectangle_area(10, 4))

# Get values from user
length = float(input("\nEnter length: "))
width = float(input("Enter width: "))
result = rectangle_area(length, width)
print(f"Area of {length} x {width} rectangle: {result}")

# Example Input:  7, 2.5
# Example Output: Area of 7.0 x 2.5 rectangle: 17.5
