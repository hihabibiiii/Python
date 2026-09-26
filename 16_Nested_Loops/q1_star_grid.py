# Question:
# Print a 5x5 grid of stars using nested loops.
#
# Expected Output:
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *

print("5x5 grid of stars:")
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()  # Move to next line after each row
