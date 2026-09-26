# Question:
# Simple login check.
# Accept username and password from user.
# Grant access only if username == "admin" AND password == "1234".

# Example:
# Enter username: admin
# Enter password: 1234
# Access granted!

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied. Invalid credentials.")
