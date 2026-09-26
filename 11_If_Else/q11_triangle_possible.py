# Question:
# Take 3 numbers from the user representing the sides of a triangle.
# A triangle is possible if the sum of any two sides is greater than the third.
# Print 'Triangle possible' or 'Triangle not possible'.
#
# Example:
#   Input: 3, 4, 5  -> Output: Triangle possible
#   Input: 1, 2, 10 -> Output: Triangle not possible

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle possible")
else:
    print("Triangle not possible")
