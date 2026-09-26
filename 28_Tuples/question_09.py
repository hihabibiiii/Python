# Question:
# Create a tuple with repeated values.
# Use count() to count how many times a specific value appears.

# Example Output:
# Tuple: (1, 2, 3, 2, 4, 2, 5)
# Count of 2: 3

data = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {data}")

val = int(input("Enter a value to count: "))
print(f"Count of {val}: {data.count(val)}")
