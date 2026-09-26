# Question:
# Use a lambda with reduce() from functools to compute the product of all numbers in a list.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print(f"Numbers: {numbers}")

product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")
