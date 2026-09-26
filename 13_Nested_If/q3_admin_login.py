# Question:
# Simulate a simple login system using nested if.
# There is only one valid admin account: username='admin', password='secret'
# - First check if username is 'admin'.
#   - If yes, check if password is 'secret'.
#     - If yes: print 'Welcome, Admin!'
#     - If no:  print 'Wrong password!'
#   - If username is not 'admin': print 'Access Denied: Not an admin account.'
#
# Example:
#   admin / secret       -> Welcome, Admin!
#   admin / wrongpass    -> Wrong password!
#   bob   / secret       -> Access Denied: Not an admin account.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "secret":
        print("Welcome, Admin!")
    else:
        print("Wrong password!")
else:
    print("Access Denied: Not an admin account.")
