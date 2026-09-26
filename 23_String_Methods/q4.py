# Question: Use split() to split a sentence into a list of words.
# split() without arguments splits on any whitespace.
# Example:
#   Input: "Python is fun to learn"
#   Output: ['Python', 'is', 'fun', 'to', 'learn']

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words list:", words)
print("Number of words:", len(words))
