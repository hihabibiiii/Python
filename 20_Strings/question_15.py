# Question:
# Take a sentence from the user.
# Print the words in reverse order.

# Example:
# Enter a sentence: Python is fun to learn
# Reversed words: learn to fun is Python

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Reversed words: ", end="")
for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
print()
