# Question 10 (Medium):
# Convert an integer to its binary, octal, and hexadecimal string representations
# using bin(), oct(), and hex() respectively.

# Solution:
number = 255

binary = bin(number)
octal = oct(number)
hexadecimal = hex(number)

print("Decimal    :", number)
print("Binary     :", binary)
print("Octal      :", octal)
print("Hexadecimal:", hexadecimal)

# Output:
# Decimal    : 255
# Binary     : 0b11111111
# Octal      : 0o377
# Hexadecimal: 0xff
