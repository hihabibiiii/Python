# Question:
# Print a right triangle pattern with numbers.
# Row i prints the number i, exactly i times.
#
# Expected Output (5 rows):
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5

print("Right triangle with numbers:")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
