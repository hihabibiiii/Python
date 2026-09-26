# Question: Check if an element is in a list using the `in` keyword.
# `in` returns True if the value exists in the list, False otherwise.
# Example:
#   List: ['maths', 'science', 'english']
#   Check: 'science' -> True
#   Check: 'history' -> False

subjects = ["maths", "science", "english", "history", "art"]
print("Subjects:", subjects)

search = input("Enter a subject to check: ")
if search in subjects:
    print(f"'{search}' is in the list!")
else:
    print(f"'{search}' is NOT in the list.")
