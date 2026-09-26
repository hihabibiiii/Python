# Question:
# Take a sentence from the user.
# Replace all spaces with underscores and print the result.

# Example:
# Enter a sentence: Hello World Python
# Result: Hello_World_Python

sentence = input("Enter a sentence: ")
result = ""
for ch in sentence:
    if ch == " ":
        result += "_"
    else:
        result += ch

print(f"Result: {result}")
