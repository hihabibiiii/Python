# Question: Use isalpha(), isdigit(), and isalnum() on different strings.
# isalpha()  -> True if all characters are alphabetic
# isdigit()  -> True if all characters are digits
# isalnum()  -> True if all characters are alphanumeric

s1 = "Hello"
s2 = "12345"
s3 = "Hello123"
s4 = "Hello World"

print(f"'{s1}'.isalpha()  = {s1.isalpha()}")
print(f"'{s1}'.isdigit()  = {s1.isdigit()}")
print(f"'{s1}'.isalnum()  = {s1.isalnum()}")
print()
print(f"'{s2}'.isalpha()  = {s2.isalpha()}")
print(f"'{s2}'.isdigit()  = {s2.isdigit()}")
print(f"'{s2}'.isalnum()  = {s2.isalnum()}")
print()
print(f"'{s3}'.isalpha()  = {s3.isalpha()}")
print(f"'{s3}'.isdigit()  = {s3.isdigit()}")
print(f"'{s3}'.isalnum()  = {s3.isalnum()}")
print()
print(f"'{s4}'.isalpha()  = {s4.isalpha()}  (space is not alpha)")
print(f"'{s4}'.isalnum()  = {s4.isalnum()}  (space is not alnum)")
