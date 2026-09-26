# Question:
# Sort a list of 8 numbers using the Bubble Sort algorithm with nested loops.
# Bubble sort repeatedly compares adjacent elements and swaps them if they are
# in the wrong order, pushing larger values to the end.
#
# numbers = [64, 34, 25, 12, 22, 11, 90, 45]
#
# Expected Output:
#   Sorted list: [11, 12, 22, 25, 34, 45, 64, 90]

numbers = [64, 34, 25, 12, 22, 11, 90, 45]
print(f"Original list: {numbers}")

n = len(numbers)

# Bubble sort: outer loop for passes, inner loop for comparisons
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # Swap the two adjacent elements
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print(f"Sorted list : {numbers}")
