# Question:
# Take a password from the user.
# If the password length is >= 8 AND it contains at least one digit, print "Strong password".

# Example:
# Enter password: secure12
# Strong password

password = input("Enter password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Strong password")
