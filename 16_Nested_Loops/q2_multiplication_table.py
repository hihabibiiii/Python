# Question:
# Print the multiplication table for numbers 1 to 5 using nested loops.
#
# Expected Output:
#   1  2  3  4  5
#   2  4  6  8 10
#   3  6  9 12 15
#   4  8 12 16 20
#   5 10 15 20 25

print("Multiplication table for 1 to 5:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")
    print()
