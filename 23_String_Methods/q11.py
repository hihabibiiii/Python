# Question: Use center(), ljust(), and rjust() to format a string for display.
# center(width) -> centers the string, padding with spaces
# ljust(width)  -> left-justifies the string, padding right with spaces
# rjust(width)  -> right-justifies the string, padding left with spaces
# Example:
#   Text: "Python", width=20
#   center: '       Python       '
#   ljust:  'Python              '
#   rjust:  '              Python'

text = input("Enter a string: ")
width = int(input("Enter the total display width: "))

print("center():", text.center(width))
print("ljust(): ", text.ljust(width))
print("rjust(): ", text.rjust(width))

# With a fill character
print("\nWith '*' as fill character:")
print("center():", text.center(width, "*"))
print("ljust(): ", text.ljust(width, "*"))
print("rjust(): ", text.rjust(width, "*"))
