# Question: Use join() to join a list of words into a sentence.
# join() is called on the separator string and takes a list as argument.
# Example:
#   Words: ['Python', 'is', 'fun']
#   Output: "Python is fun"

words = ["Python", "is", "fun", "to", "learn"]
print("Word list:", words)

sentence = " ".join(words)
print("Joined sentence:", sentence)

# Also demonstrate joining with a different separator
csv_line = ", ".join(words)
print("Joined with comma:", csv_line)
