# Question: Slice the middle elements of a list, excluding the first and last element.
# Use [1:-1] to skip the first and last.
# Example:
#   List: [10, 20, 30, 40, 50]
#   Middle (excluding first and last): [20, 30, 40]

numbers = [10, 20, 30, 40, 50]
print("Full list:", numbers)
middle = numbers[1:-1]
print("Middle elements (excluding first and last):", middle)
