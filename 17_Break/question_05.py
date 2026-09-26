# Question:
# Simulate a login system with 3 attempts.
# Keep asking for username and password.
# Use break if the correct credentials are entered.
# Correct credentials: username = "admin", password = "pass123"

# Example:
# Attempt 1
# Username: admin
# Password: pass123
# Login successful!

correct_user = "admin"
correct_pass = "pass123"

for attempt in range(1, 4):
    print(f"Attempt {attempt}")
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_user and password == correct_pass:
        print("Login successful!")
        break
    else:
        print("Incorrect credentials. Try again.\n")
else:
    print("Account locked after 3 failed attempts.")
