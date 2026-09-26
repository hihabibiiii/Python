# Question:
# Take a number from the user.
# Repeatedly halve the number using a while loop until it is less than 1.
# Count and print the number of steps.
# This demonstrates how the logarithm (log base 2) works.
#
# Example:
#   Input: 16
#   Steps: 16 -> 8.0 -> 4.0 -> 2.0 -> 1.0 -> 0.5
#   Output: It took 5 steps to halve 16 below 1.

number = float(input("Enter a positive number: "))
original = number

steps = 0
print(f"Starting value: {number}")

while number >= 1:
    number = number / 2
    steps = steps + 1
    print(f"  Step {steps}: {number}")

print(f"\nIt took {steps} step(s) to halve {original} below 1.")
print(f"(This is related to log2({original}) ≈ {steps - 1})")
