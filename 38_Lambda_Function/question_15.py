# Question:
# Create two lambdas: one that doubles a number, one that squares it.
# Compose them in two ways:
#   1. double then square: (x*2)^2
#   2. square then double: (x^2)*2
# Compare the results.

double = lambda x: x * 2
square = lambda x: x ** 2

x = 3
print(f"x = {x}")
print(f"double(x) = {double(x)}")
print(f"square(x) = {square(x)}")

# double then square
ds = square(double(x))
print(f"\ndouble then square: square(double({x})) = square({double(x)}) = {ds}")

# square then double
sd = double(square(x))
print(f"square then double: double(square({x})) = double({square(x)}) = {sd}")

print(f"\nAre they the same? {ds == sd}")
