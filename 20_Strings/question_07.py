# Question:
# Take a string from the user and print it reversed.
# Use a loop to reverse (do not use slicing or reversed()).

# Example:
# Enter a string: Python
# Reversed: nohtyP

text = input("Enter a string: ")

reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text

print(f"Reversed: {reversed_text}")
