# Question: Use extend() to add multiple items from another list.
# extend() adds ALL items from an iterable to the end of the list.
# Example:
#   list1 = [1, 2, 3]
#   list1.extend([4, 5, 6])
#   Result: [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("list1 before extend:", list1)
print("list2:", list2)

list1.extend(list2)
print("list1 after extend(list2):", list1)

# Difference from append: extend adds each item individually
list3 = [10, 20]
list3.append([30, 40])   # appends as a single item (nested list)
list4 = [10, 20]
list4.extend([30, 40])   # extends with each item separately
print("\nappend([30,40]) ->", list3)
print("extend([30,40]) ->", list4)
