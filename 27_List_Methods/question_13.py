# Question:
# Demonstrate the difference between sort() and sorted().
# sort() modifies the list in place; sorted() returns a NEW list.

# Example Output:
# Original: [5, 2, 8, 1, 9, 3]
# After sorted(): [1, 2, 3, 5, 8, 9]  (original unchanged)
# After sort(): [1, 2, 3, 5, 8, 9]   (original is modified)

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")

new_list = sorted(numbers)
print(f"sorted() result (new list): {new_list}")
print(f"Original after sorted(): {numbers}  <- unchanged!")

numbers.sort()
print(f"After sort() (in-place): {numbers}  <- original is now sorted")
