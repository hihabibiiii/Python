# Question:
# Ask the user to enter 10 numbers one by one.
# Skip (ignore) negative numbers using `continue`.
# Compute and print the sum of positive numbers only.

# Example:
# Enter number 1: 5
# Enter number 2: -3  <- skipped
# ...
# Sum of positives = ...

total = 0
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    if num < 0:
        print("  (Skipping negative number)")
        continue
    total += num

print(f"Sum of positive numbers = {total}")
