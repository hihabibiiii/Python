# Question:
# Take two strings from the user.
# Print which string comes first alphabetically,
# or print 'Same' if they are identical.
#
# Example:
#   Input: apple, banana  -> Output: apple comes first
#   Input: mango, apple   -> Output: apple comes first
#   Input: hello, hello   -> Output: Same

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if str1 == str2:
    print("Same")
else:
    if str1 < str2:
        print(f"'{str1}' comes first alphabetically")
    else:
        print(f"'{str2}' comes first alphabetically")
