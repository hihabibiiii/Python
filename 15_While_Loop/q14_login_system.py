# Question:
# Simulate a login system with a maximum of 3 attempts using a while loop.
# Correct credentials: username = 'admin', password = 'password123'
# - Allow up to 3 attempts.
# - If correct: print 'Login successful!'
# - If all 3 attempts fail: print 'Account locked!'
#
# Example:
#   Attempt 1: wrong/wrong  -> Invalid. 2 attempts remaining.
#   Attempt 2: wrong/wrong  -> Invalid. 1 attempt remaining.
#   Attempt 3: wrong/wrong  -> Account locked!

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"
MAX_ATTEMPTS = 3

attempt = 0
logged_in = False

print("=== Login System ===")

while attempt < MAX_ATTEMPTS:
    attempt = attempt + 1
    username = input(f"\nAttempt {attempt}/{MAX_ATTEMPTS} - Username: ")
    password = input("Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Login successful! Welcome, Admin.")
        logged_in = True
        break
    else:
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Invalid credentials! {remaining} attempt(s) remaining.")
        else:
            print("Invalid credentials!")

if not logged_in:
    print("Account locked! Too many failed attempts.")
