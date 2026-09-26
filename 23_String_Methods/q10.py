# Question: Use title(), capitalize(), and swapcase() on a string.
# title()      -> Capitalizes first letter of each word
# capitalize() -> Capitalizes only the very first character
# swapcase()   -> Swaps uppercase to lowercase and vice versa
# Example:
#   Input: "hello WORLD python"
#   title():      Hello World Python
#   capitalize(): Hello world python
#   swapcase():   HELLO world PYTHON

text = input("Enter a string: ")
print("title():     ", text.title())
print("capitalize():", text.capitalize())
print("swapcase():  ", text.swapcase())
