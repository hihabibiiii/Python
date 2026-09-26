# Question:
# Take a number n from the user and print the first n terms of the
# Fibonacci sequence using a for loop.
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each term is the sum of the two preceding terms.
#
# Example:
#   Input: 8
#   Output: 0 1 1 2 3 5 8 13

n = int(input("Enter the number of Fibonacci terms to display: "))

a = 0
b = 1

print(f"First {n} terms of the Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp

print()  # Move to the next line after the sequence
