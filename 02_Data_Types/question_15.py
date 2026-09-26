# Question 15 (Hard):
# Take a number from the user as a string (input() always returns str).
# Convert it to int and float.
# Demonstrate arithmetic operations on all three versions (str, int, float).

# Solution:
user_input = input("Enter a whole number: ")   # e.g. "7"

# Original string
str_version = user_input
print("String version:", str_version, "| Type:", type(str_version))
print("String * 3 (repetition):", str_version * 3)

# Integer version
int_version = int(user_input)
print("\nInt version:", int_version, "| Type:", type(int_version))
print("Int + 10:", int_version + 10)

# Float version
float_version = float(user_input)
print("\nFloat version:", float_version, "| Type:", type(float_version))
print("Float / 2:", float_version / 2)

# Example Input / Output:
# Enter a whole number: 7
# String version: 7 | Type: <class 'str'>
# String * 3 (repetition): 777
# Int version: 7 | Type: <class 'int'>
# Int + 10: 17
# Float version: 7.0 | Type: <class 'float'>
# Float / 2: 3.5
