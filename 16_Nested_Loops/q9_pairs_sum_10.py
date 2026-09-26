# Question:
# Find all pairs (i, j) where i + j == 10, for i and j in the range 0 to 10.
# Use nested loops to find all such pairs.
#
# Expected Output:
#   Pairs (i, j) where i + j = 10:
#   (0, 10)
#   (1, 9)
#   (2, 8)
#   (3, 7)
#   (4, 6)
#   (5, 5)
#   (6, 4)
#   (7, 3)
#   (8, 2)
#   (9, 1)
#   (10, 0)

print("Pairs (i, j) where i + j = 10:")
for i in range(0, 11):
    for j in range(0, 11):
        if i + j == 10:
            print(f"  ({i}, {j})")
