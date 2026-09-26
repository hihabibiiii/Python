# Question:
# Simulate a door lock system.
# The door opens if:
#   (card_valid AND pin_correct) OR master_key_used
# Take inputs from user.

# Example:
# Is card valid? (yes/no): yes
# Is PIN correct? (yes/no): no
# Is master key used? (yes/no): yes
# Door opened!

card_valid = input("Is card valid? (yes/no): ").strip().lower() == "yes"
pin_correct = input("Is PIN correct? (yes/no): ").strip().lower() == "yes"
master_key = input("Is master key used? (yes/no): ").strip().lower() == "yes"

if (card_valid and pin_correct) or master_key:
    print("Door opened!")
else:
    print("Access denied. Door remains locked.")
