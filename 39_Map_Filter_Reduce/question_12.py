# Question:
# Use reduce() to compute the factorial of a number.
# factorial(n) = 1 * 2 * 3 * ... * n

from functools import reduce

n = int(input("Enter a number: "))
if n <= 0:
    print("Factorial is 1 for 0, undefined for negatives.")
else:
    factorial = reduce(lambda x, y: x * y, range(1, n + 1))
    print(f"{n}! = {factorial}")
