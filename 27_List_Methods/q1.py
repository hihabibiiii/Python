# Question: Use append() to add items to a list one at a time.
# append() adds a single item to the END of the list.
# Example:
#   Start with [], append 'a', 'b', 'c'
#   Result: ['a', 'b', 'c']

my_list = []
print("Starting with empty list:", my_list)

items = ["apple", "banana", "cherry"]
for item in items:
    my_list.append(item)
    print(f"After append('{item}'): {my_list}")
