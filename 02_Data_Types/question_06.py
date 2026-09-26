# Question 6 (Medium):
# Take a number from the user as input.
# Determine whether it is an integer or a float by checking its type
# and its value. Print an appropriate message.

# Solution:
user_input = input("Enter a number: ")

# Try to interpret as int first, then as float
if "." in user_input:
    number = float(user_input)
    print("You entered a float:", number)
else:
    number = int(user_input)
    print("You entered an integer:", number)

print("Type:", type(number))

# Example Input / Output:
# Enter a number: 7
# You entered an integer: 7
# Type: <class 'int'>

# Enter a number: 3.5
# You entered a float: 3.5
# Type: <class 'float'>
