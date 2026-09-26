# Question:
# Find all 3-digit Armstrong numbers using nested loops.
# A 3-digit Armstrong number = sum of cubes of its digits.
# Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#
# Use nested loops:
#   Outer loop: range 100 to 999
#   Inner loop: extract each digit (hundreds, tens, units)
#
# Expected Output: 153, 370, 371, 407

print("3-digit Armstrong numbers:")
armstrong_numbers = []

for num in range(100, 1000):
    # Extract digits using integer division and modulo
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    # Compute sum of cubes of digits
    cube_sum = 0
    digits = [hundreds, tens, units]
    for digit in digits:
        cube_sum = cube_sum + (digit ** 3)

    if cube_sum == num:
        armstrong_numbers.append(num)

print(", ".join(str(n) for n in armstrong_numbers))
