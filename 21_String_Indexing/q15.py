# Question: Given a string, print characters at even indices in their original order,
#           then print characters at odd indices in their original order.
# Example:
#   Input: "Python"
#   Even indices (0,2,4): P t o  -> "Pto"
#   Odd indices  (1,3,5): y h n  -> "yhn"

text = input("Enter a string: ")

even_chars = ""
odd_chars = ""

for i in range(len(text)):
    if i % 2 == 0:
        even_chars += text[i]
    else:
        odd_chars += text[i]

print("Characters at even indices:", even_chars)
print("Characters at odd indices:", odd_chars)
