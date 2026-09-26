# Question: Use pop() to remove and return the last item from a list.
# pop() with no argument removes the LAST element and returns it.
# pop(index) removes the element at the given index and returns it.
# Example:
#   List: [10, 20, 30, 40, 50]
#   pop() -> returns 50, list becomes [10, 20, 30, 40]

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

popped = numbers.pop()
print(f"Popped item: {popped}")
print("List after pop():", numbers)

# pop at specific index
popped_index = numbers.pop(1)
print(f"\nPopped item at index 1: {popped_index}")
print("List after pop(1):", numbers)
