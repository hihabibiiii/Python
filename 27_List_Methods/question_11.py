# Question:
# Use clear() to empty a list, then rebuild it by appending new items.
# Show the list before and after clearing.

# Example Output:
# Before clear: [1, 2, 3, 4, 5]
# After clear: []
# After rebuilding: [10, 20, 30]

numbers = [1, 2, 3, 4, 5]
print(f"Before clear: {numbers}")

numbers.clear()
print(f"After clear: {numbers}")

numbers.append(10)
numbers.append(20)
numbers.append(30)
print(f"After rebuilding: {numbers}")
