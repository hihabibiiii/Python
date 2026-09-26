# Question:
# Print a checkerboard pattern of 0s and 1s for an 8x8 grid using nested loops.
# The pattern alternates between 0 and 1 like a chess board.
#
# Expected Output (8x8):
#   0 1 0 1 0 1 0 1
#   1 0 1 0 1 0 1 0
#   0 1 0 1 0 1 0 1
#   ...

SIZE = 8
print(f"{SIZE}x{SIZE} Checkerboard pattern:")
for row in range(SIZE):
    for col in range(SIZE):
        # If sum of row and col is even -> 0, else -> 1
        if (row + col) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()
