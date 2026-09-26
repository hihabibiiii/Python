# Question:
# Take a number from the user.
# Classify it as:
#   - Perfect square (e.g., 4, 9, 16)
#   - Perfect cube (e.g., 8, 27, 64)
#   - Both (e.g., 64 = 8^2 and 4^3)
#   - Neither
#
# Hint: Use integer square root and cube root checks.
#
# Example:
#   Input: 64  -> Output: Both a perfect square and a perfect cube
#   Input: 16  -> Output: Perfect square
#   Input: 27  -> Output: Perfect cube
#   Input: 10  -> Output: Neither

number = int(input("Enter a positive integer: "))

# Check perfect square
sqrt_n = int(number ** 0.5)
is_perfect_square = (sqrt_n * sqrt_n == number)

# Check perfect cube
cbrt_n = round(number ** (1 / 3))
is_perfect_cube = (cbrt_n * cbrt_n * cbrt_n == number)

if is_perfect_square and is_perfect_cube:
    print(f"{number} is both a perfect square and a perfect cube.")
elif is_perfect_square:
    print(f"{number} is a perfect square.")
elif is_perfect_cube:
    print(f"{number} is a perfect cube.")
else:
    print(f"{number} is neither a perfect square nor a perfect cube.")
