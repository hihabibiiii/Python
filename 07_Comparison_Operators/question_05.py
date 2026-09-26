# Question 5 (Easy):
# Take two people's ages from the user.
# Compare them and print who is older, or if they are the same age.

# Solution:
name1 = input("Enter first person's name : ")
age1 = int(input(f"Enter {name1}'s age: "))

name2 = input("Enter second person's name: ")
age2 = int(input(f"Enter {name2}'s age: "))

if age1 > age2:
    print(f"{name1} (age {age1}) is older than {name2} (age {age2}).")
elif age2 > age1:
    print(f"{name2} (age {age2}) is older than {name1} (age {age1}).")
else:
    print(f"{name1} and {name2} are the same age ({age1}).")

# Example:
# Alice (25) is older than Bob (22)
