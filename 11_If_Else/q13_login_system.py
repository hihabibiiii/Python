# Question:
# Simulate a simple login system.
# Correct credentials: username = 'admin', password = 'python123'
# Ask the user for a username and password.
# - If both are correct: print 'Login successful! Welcome, admin.'
# - If username is wrong: print 'Username wrong'
# - If username is correct but password is wrong: print 'Password wrong'
#
# Example:
#   Input: admin, python123  -> Output: Login successful! Welcome, admin.
#   Input: user, python123   -> Output: Username wrong
#   Input: admin, wrongpass  -> Output: Password wrong

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "python123"

entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

if entered_username == CORRECT_USERNAME:
    if entered_password == CORRECT_PASSWORD:
        print("Login successful! Welcome, admin.")
    else:
        print("Password wrong")
else:
    print("Username wrong")
