# Question 11 (Hard):
# Create a dictionary of squares where:
#   - Keys are numbers 1 through 10
#   - Values are their squares (e.g. {1: 1, 2: 4, 3: 9, ..., 10: 100})
# Print the dictionary and then print each key-value pair neatly.

# Solution:
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2

print("Squares dictionary:", squares)

print("\nDetailed view:")
print(f"{'Number':<10} {'Square':<10}")
print("-" * 20)
for num, sq in squares.items():
    print(f"{num:<10} {sq:<10}")

# Example Output:
# Squares dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#
# Detailed view:
# Number     Square
# --------------------
# 1          1
# 2          4
# ...
# 10         100
