# Question: Access an element at an index specified by the user.
# Example:
#   List: ['red', 'green', 'blue', 'yellow', 'purple']
#   Index: 2 -> Output: blue

colors = ["red", "green", "blue", "yellow", "purple"]
print("List:", colors)

index = int(input("Enter the index you want to access: "))
print(f"Element at index {index}:", colors[index])
