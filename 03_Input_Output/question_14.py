# Question 14 (Hard):
# Take the user's name and birth year as input.
# Compute their approximate age (use 2025 as the current year).
# Print a formatted biography string.

# Solution:
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2025
age = current_year - birth_year

print(f"\n--- Biography ---")
print(f"Name       : {name}")
print(f"Birth Year : {birth_year}")
print(f"Age        : {age} years old")
print(f"{name} was born in {birth_year} and is approximately {age} years old.")

# Example Input / Output:
# Enter your name: Alex
# Enter your birth year: 2000
#
# --- Biography ---
# Name       : Alex
# Birth Year : 2000
# Age        : 25 years old
# Alex was born in 2000 and is approximately 25 years old.
