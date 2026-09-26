# Question:
# Given a list of numbers, replace all negative values with 0.
# Use a conditional expression inside list comprehension.

data = [-3, 5, -1, 8, -7, 2, 0, -4, 9, -6]
print(f"Original: {data}")

cleaned = [x if x >= 0 else 0 for x in data]
print(f"Negatives replaced with 0: {cleaned}")
