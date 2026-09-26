# Question: Print elements from index 1 to 3 (inclusive) using indexing in a loop.
# Use a for loop with range to iterate over the specific indices.
# Example:
#   List: [10, 20, 30, 40, 50]
#   Indices 1 to 3: 20, 30, 40

numbers = [10, 20, 30, 40, 50]
print("Full list:", numbers)

print("\nElements at indices 1, 2, 3:")
for i in range(1, 4):  # indices 1, 2, 3
    print(f"  Index {i}: {numbers[i]}")
