# Question:
# Take a list with duplicate values.
# Convert to a set to remove duplicates.
# Convert back to a list and print.
# Also compare lengths.

original_list = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4, 7]
print(f"Original list: {original_list}")
print(f"Length: {len(original_list)}")

unique_set = set(original_list)
unique_list = list(unique_set)

print(f"After deduplication: {sorted(unique_list)}")
print(f"Unique elements: {len(unique_list)}")
print(f"Duplicates removed: {len(original_list) - len(unique_list)}")
