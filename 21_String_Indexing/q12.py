# Question: Take a string and print every 2nd character using indexing in a loop.
# Use a loop with a step to access characters at even indices (0, 2, 4, ...).
# Example:
#   Input: "Python"
#   Output: P t o

text = input("Enter a string: ")
print("Every 2nd character (at indices 0, 2, 4, ...):")

result = ""
for i in range(0, len(text), 2):
    result += text[i]

print(result)
