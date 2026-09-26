# Question:
# Chain map() and filter():
# From a list of numbers, get only even numbers, then square each of them.

numbers = list(range(1, 21))
print(f"Numbers 1-20: {numbers}")

# Step 1: Filter evens
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Map to squares
squares_of_evens = list(map(lambda x: x**2, evens))

print(f"Squares of even numbers: {squares_of_evens}")
