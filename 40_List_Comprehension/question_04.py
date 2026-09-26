# Question:
# Given a list of numbers (positive and negative), use list comprehension
# to keep only the positive numbers.

data = [-3, 5, -1, 8, -7, 2, 0, 4, -9, 6]
print(f"Original: {data}")

positives = [x for x in data if x > 0]
print(f"Positives: {positives}")
