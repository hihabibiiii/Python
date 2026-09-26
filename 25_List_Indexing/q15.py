# Question: Reverse a list using indexing (loop from the end to the start)
#           WITHOUT using reverse() or slicing.
# Use a loop that starts at the last index and goes down to 0.
# Example:
#   Original: [1, 2, 3, 4, 5]
#   Reversed: [5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list (using indexing):", reversed_list)
