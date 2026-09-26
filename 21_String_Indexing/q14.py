# Question: Find all indices where a specific character appears in a string using a loop.
# Iterate through the string and collect every index where the character matches.
# Example:
#   String: "mississippi"
#   Character: "s"
#   Output: 's' found at indices: [2, 3, 5, 6]

text = input("Enter a string: ")
char = input("Enter the character to search for: ")

indices = []
for i in range(len(text)):
    if text[i] == char:
        indices.append(i)

if indices:
    print(f"'{char}' found at indices: {indices}")
else:
    print(f"'{char}' was not found in the string.")
