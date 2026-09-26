# Question 14 (Hard):
# Take a number from the user.
# Use bitwise AND (&) with 1 to check if the number is even or odd.
# (If n & 1 == 0, it's even; if n & 1 == 1, it's odd.)
# Print the result with an explanation.

# Solution:
number = int(input("Enter an integer: "))

bit_result = number & 1    # Check the least significant bit

if bit_result == 0:
    print(f"{number} is EVEN  (binary: {bin(number)}, last bit = 0)")
else:
    print(f"{number} is ODD   (binary: {bin(number)}, last bit = 1)")

# Example Input / Output:
# Enter an integer: 7
# 7 is ODD   (binary: 0b111, last bit = 1)

# Enter an integer: 12
# 12 is EVEN  (binary: 0b1100, last bit = 0)
