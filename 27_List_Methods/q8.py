# Question: Use sort() to sort a list of numbers in ascending and descending order.
# sort() modifies the list IN PLACE (no new list is created).
# Example:
#   Before: [34, 7, 23, 32, 5, 62]
#   Ascending:  [5, 7, 23, 32, 34, 62]
#   Descending: [62, 34, 32, 23, 7, 5]

numbers = [34, 7, 23, 32, 5, 62]
print("Original list:", numbers)

numbers.sort()
print("After sort() (ascending):", numbers)

numbers.sort(reverse=True)
print("After sort(reverse=True) (descending):", numbers)
