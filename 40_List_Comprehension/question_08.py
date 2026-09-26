# Question:
# From numbers 1 to 20, get only odd numbers and square each of them.
# Use a single list comprehension with a condition and transformation.

squared_odds = [x**2 for x in range(1, 21) if x % 2 != 0]
print(f"Squares of odd numbers 1-20: {squared_odds}")
