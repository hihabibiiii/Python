# Question: Use reverse() to reverse a list in place.
# reverse() modifies the original list (no new list is created).
# Example:
#   Before: [1, 2, 3, 4, 5]
#   After:  [5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.reverse()
print("After reverse():", numbers)

# Demonstrate it modifies in place (original is changed)
words = ["hello", "world", "python"]
print("\nWords before:", words)
words.reverse()
print("Words after reverse():", words)
