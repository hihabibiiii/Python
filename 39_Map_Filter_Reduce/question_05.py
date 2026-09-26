# Question:
# Use reduce() from functools to compute the sum of all numbers in a list.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

total = reduce(lambda x, y: x + y, numbers)
print(f"Sum (using reduce): {total}")
