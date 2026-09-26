# Question:
# Take a word from the user and repeat it 3 times using the * operator.
# Print with a space between repetitions.

# Example:
# Enter a word: Hello
# Hello Hello Hello

word = input("Enter a word: ")
result = (word + " ") * 3
print(result.strip())
