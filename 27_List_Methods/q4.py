# Question: Use remove() to delete a specific value from a list.
# remove() deletes the FIRST occurrence of the specified value.
# If value not found, it raises ValueError.
# Example:
#   Before: [3, 1, 4, 1, 5, 9]
#   remove(1)
#   After:  [3, 4, 1, 5, 9]  (only first '1' removed)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", numbers)

numbers.remove(1)
print("After remove(1) - removes first occurrence:", numbers)

# Handle case where value is not in list
try:
    numbers.remove(100)
except ValueError:
    print("ValueError: 100 is not in the list.")
