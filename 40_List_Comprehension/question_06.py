# Question:
# Flatten a 2D list using nested list comprehension.
# [[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6]

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(f"Original 2D list: {matrix}")

flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")
