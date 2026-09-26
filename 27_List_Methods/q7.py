# Question: Use count() to count how many times a value appears in a list.
# count(value) returns the number of occurrences of value in the list.
# Example:
#   List: [1, 2, 3, 2, 4, 2, 5]
#   count(2) -> 3

numbers = [1, 2, 3, 2, 4, 2, 5, 1, 1]
print("List:", numbers)

print(f"count(2): {numbers.count(2)}")
print(f"count(1): {numbers.count(1)}")
print(f"count(9): {numbers.count(9)}  (9 is not in the list)")
