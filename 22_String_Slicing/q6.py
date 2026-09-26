# Question: Take a string and print its first half and second half using slicing.
# Use integer division to find the midpoint.
# Example:
#   Input: "Python"  (length 6, mid=3)
#   First half:  "Pyt"
#   Second half: "hon"

text = input("Enter a string: ")
mid = len(text) // 2
first_half = text[:mid]
second_half = text[mid:]
print("First half:", first_half)
print("Second half:", second_half)
