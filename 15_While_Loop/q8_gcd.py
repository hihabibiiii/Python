# Question:
# Compute the GCD (Greatest Common Divisor) of two numbers using the
# Euclidean algorithm with a while loop.
# Euclidean Algorithm: GCD(a, b) = GCD(b, a % b), until b = 0.
#
# Example:
#   Input: 48, 18  -> Output: GCD = 6
#   Input: 100, 75 -> Output: GCD = 25

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

original_a = a
original_b = b

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(f"GCD of {original_a} and {original_b} = {a}")
