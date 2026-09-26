# Question: Remove an element from a list by its value using remove().
# remove() deletes the FIRST occurrence of the specified value.
# Example:
#   List: ['apple', 'banana', 'cherry', 'banana']
#   Remove: 'banana'
#   Result: ['apple', 'cherry', 'banana']

fruits = ["apple", "banana", "cherry", "banana"]
print("Original list:", fruits)

item = input("Enter the item to remove: ")
if item in fruits:
    fruits.remove(item)
    print("After removing:", fruits)
else:
    print(f"'{item}' not found in the list.")
