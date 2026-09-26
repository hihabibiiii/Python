# Question:
# Use reduce() to find the maximum value in a list (without using max()).

from functools import reduce

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Numbers: {numbers}")

maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum (using reduce): {maximum}")
