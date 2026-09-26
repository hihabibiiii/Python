# Question:
# Print Floyd's Triangle using nested loops.
# Floyd's triangle is a right triangle of consecutive natural numbers.
#
# Expected Output (5 rows):
#   1
#   2  3
#   4  5  6
#   7  8  9 10
#  11 12 13 14 15

print("Floyd's Triangle:")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(f"{num:3}", end="")
        num = num + 1
    print()
