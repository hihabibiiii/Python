# Question: Add an element to the end of a list using append().
# append() adds a single item to the end of the list.
# Example:
#   Before: ['cat', 'dog', 'bird']
#   After:  ['cat', 'dog', 'bird', 'fish']

animals = ["cat", "dog", "bird"]
print("Original list:", animals)

new_animal = input("Enter an animal to add: ")
animals.append(new_animal)

print("After appending:", animals)
