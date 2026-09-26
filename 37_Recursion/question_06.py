# Question:
# Write a recursive function to reverse a string.
# reverse("hello") = "olleh"

# Example:
# Enter a string: Python
# Reversed: nohtyP

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

text = input("Enter a string: ")
print(f"Reversed: {reverse_string(text)}")
