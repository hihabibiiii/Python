# Question:
# Use filter() to get only even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"Original: {numbers}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")
