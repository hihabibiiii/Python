# Question:
# Check eligibility for voting.
# A person must be age >= 18 AND have a valid ID.
# Take age and has_id (yes/no) from the user.

# Example:
# Enter age: 20
# Do you have a valid ID? (yes/no): yes
# Eligible to vote.

age = int(input("Enter age: "))
has_id = input("Do you have a valid ID? (yes/no): ").strip().lower()

if age >= 18 and has_id == "yes":
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
