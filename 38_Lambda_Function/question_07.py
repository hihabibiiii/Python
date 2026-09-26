# Question:
# Use a lambda with filter() to keep only even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens:    {evens}")
