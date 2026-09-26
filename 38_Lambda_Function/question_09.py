# Question:
# Create a lambda that computes the absolute value of a number
# WITHOUT using the built-in abs() function.

my_abs = lambda x: x if x >= 0 else -x

print(f"Absolute value of  5: {my_abs(5)}")
print(f"Absolute value of -7: {my_abs(-7)}")
print(f"Absolute value of  0: {my_abs(0)}")
