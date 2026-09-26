# Question:
# Use map() to compute the square of each element in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

squares = list(map(lambda x: x**2, numbers))
print(f"Squares:  {squares}")
