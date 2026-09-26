# Question:
# Use filter() to get only positive numbers from a list.

numbers = [-3, 0, 5, -1, 8, -7, 2, 0, 4, -9]
print(f"Original: {numbers}")

positives = list(filter(lambda x: x > 0, numbers))
print(f"Positives: {positives}")
