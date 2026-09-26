# Question:
# Use map() with TWO lists to add corresponding elements.
# map(func, list1, list2) applies func to paired elements.

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print(f"List 1: {list1}")
print(f"List 2: {list2}")

result = list(map(lambda x, y: x + y, list1, list2))
print(f"Element-wise sum: {result}")
