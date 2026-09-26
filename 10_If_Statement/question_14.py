# Question:
# Take a sentence from the user.
# If the sentence starts with a capital letter AND ends with a period ("."),
# print "Proper sentence".

# Example:
# Enter a sentence: Hello world.
# Proper sentence

sentence = input("Enter a sentence: ")

if sentence and sentence[0].isupper() and sentence.endswith("."):
    print("Proper sentence")
