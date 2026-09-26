# Question 12 (Hard):
# Create a counter using CLOSURE: a nonlocal variable captured by an inner function.
# The inner function remembers and updates the count across calls.

# Solution:
def make_counter(start=0):
    """Returns an inner function that increments and returns a count."""
    count = start   # enclosing variable (closed over)

    def counter():
        nonlocal count
        count += 1
        return count

    return counter   # return the inner function itself

# Create two independent counters
counter1 = make_counter()
counter2 = make_counter(100)

print("counter1 calls:")
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print("\ncounter2 calls (starts at 100):")
print(counter2())  # 101
print(counter2())  # 102

print("\ncounter1 is not affected by counter2:")
print(counter1())  # 4

# Example Output:
# counter1 calls:
# 1
# 2
# 3
# counter2 calls (starts at 100):
# 101
# 102
# counter1 is not affected by counter2:
# 4
