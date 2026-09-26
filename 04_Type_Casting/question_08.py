# Question 8 (Medium):
# Create a list with duplicate values.
# Convert it to a set to automatically remove duplicates.
# Print the original list and the resulting set.

# Solution:
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print("Original list (with duplicates):", my_list)

my_set = set(my_list)
print("After converting to set        :", my_set)
print("Note: Sets remove duplicates and do not preserve order.")

# Output:
# Original list (with duplicates): [1, 2, 2, 3, 4, 4, 4, 5, 1]
# After converting to set        : {1, 2, 3, 4, 5}
# Note: Sets remove duplicates and do not preserve order.
