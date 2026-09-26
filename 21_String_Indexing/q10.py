# Question: Find and print the index of a specific character in a string (first occurrence)
#           using the index() method.
# Example:
#   String: "programming"
#   Character: "g"
#   Output: First occurrence of 'g' is at index 3

text = input("Enter a string: ")
char = input("Enter the character to find: ")

if char in text:
    position = text.index(char)
    print(f"First occurrence of '{char}' is at index {position}")
else:
    print(f"'{char}' was not found in the string.")
