# Question: Reverse every word in a sentence using slicing.
# Split the sentence into words, reverse each word with [::-1], then rejoin.
# Example:
#   Input: "Hello World Python"
#   Output: olleH dlroW nohtyP

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
result = " ".join(reversed_words)
print("Sentence with each word reversed:", result)
