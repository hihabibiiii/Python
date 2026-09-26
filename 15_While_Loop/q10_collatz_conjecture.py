# Question:
# The Collatz Conjecture:
# Take a positive integer n from the user.
# Apply these rules repeatedly until you reach 1:
#   - If n is even: n = n // 2
#   - If n is odd:  n = 3 * n + 1
# Count and print the number of steps taken to reach 1.
#
# Example:
#   Input: 6
#   Sequence: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#   Output: Steps = 8

n = int(input("Enter a positive integer: "))
original = n

steps = 0
print(f"Collatz sequence starting from {n}:")
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f" -> {n}", end="")
    steps = steps + 1

print(f"\n\nNumber of steps to reach 1: {steps}")
