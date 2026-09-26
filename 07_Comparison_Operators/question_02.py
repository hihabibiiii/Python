# Question 2 (Easy):
# Take two strings from the user.
# Check if they are exactly equal (case-sensitive) using ==.
# Print whether they match.

# Solution:
str1 = input("Enter first string : ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("The strings are equal (case-sensitive match).")
else:
    print("The strings are NOT equal.")
    print(f"  '{str1}' != '{str2}'")

# Example:
# "Python" == "Python"  -> equal
# "Python" == "python"  -> not equal (case-sensitive)
