# Question:
# Take three numbers a, b, c from the user.
# If a^2 + b^2 == c^2, print "Pythagorean triple".
# (They form a right triangle.)

# Example:
# Enter a: 3
# Enter b: 4
# Enter c: 5
# Pythagorean triple

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a**2 + b**2 == c**2:
    print("Pythagorean triple")
