# Question 12 (Hard):
# Take a string from the user.
# Compare its length to 10:
#   length < 5          : "Short"
#   length 5-10         : "Medium"
#   length > 10         : "Long"

# Solution:
text = input("Enter a string: ")
length = len(text)

if length < 5:
    category = "Short"
elif length <= 10:
    category = "Medium"
else:
    category = "Long"

print(f"String  : '{text}'")
print(f"Length  : {length} characters")
print(f"Category: {category}")

# Example:
# "hi"          -> Short  (2 chars)
# "Hello"       -> Medium (5 chars)
# "Hello World" -> Long   (11 chars)
