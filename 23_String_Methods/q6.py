# Question: Use find() and index() to locate a substring within a string.
# find() returns -1 if not found; index() raises ValueError if not found.
# Example:
#   String: "Hello, World!"
#   Substring: "World"
#   find()  result: 7
#   index() result: 7

text = input("Enter a string: ")
sub = input("Enter the substring to find: ")

find_result = text.find(sub)
print(f"find('{sub}') returned: {find_result}")
if find_result == -1:
    print("  -> Substring not found (find returns -1).")
else:
    print(f"  -> Found at index {find_result}.")

try:
    index_result = text.index(sub)
    print(f"index('{sub}') returned: {index_result}")
except ValueError:
    print(f"index('{sub}') raised ValueError: substring not found.")
