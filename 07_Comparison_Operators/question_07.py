# Question 7 (Medium):
# Take three numbers from the user.
# Find and print the largest using only comparison operators and if statements.

# Solution:
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
c = float(input("Enter third number : "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"\nNumbers: {a}, {b}, {c}")
print(f"Largest: {largest}")

# Example:
# 4, 9, 6 -> Largest: 9
