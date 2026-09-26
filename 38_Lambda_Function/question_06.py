# Question:
# Use a lambda with map() to double all elements of a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original: {numbers}")

doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled:  {doubled}")
