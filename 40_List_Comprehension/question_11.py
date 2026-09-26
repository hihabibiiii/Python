# Question:
# Create a 5x5 multiplication table as a 2D list using nested list comprehension.
# Print it formatted.

table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print("5x5 Multiplication Table:")
print("    ", "  ".join(f"{j:3}" for j in range(1, 6)))
print("   " + "-" * 20)
for i, row in enumerate(table, 1):
    print(f" {i} |", "  ".join(f"{val:3}" for val in row))
