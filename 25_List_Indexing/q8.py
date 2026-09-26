# Question: Find the index of a specific value in a list using the index() method.
# index() returns the position of the FIRST occurrence of the value.
# Example:
#   List: ['banana', 'apple', 'cherry', 'apple']
#   Value: 'apple' -> Index: 1

fruits = ["banana", "apple", "cherry", "mango", "apple"]
print("List:", fruits)

search = input("Enter the value to find: ")
if search in fruits:
    position = fruits.index(search)
    print(f"'{search}' is at index: {position}")
else:
    print(f"'{search}' not found in the list.")
