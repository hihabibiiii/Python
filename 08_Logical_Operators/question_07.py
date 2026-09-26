# Question:
# Take a number from the user and check if it is divisible by 2 OR by 3.
# Print appropriate messages for each case.

# Example:
# Enter a number: 6
# 6 is divisible by 2.
# 6 is divisible by 3.

num = int(input("Enter a number: "))

if num % 2 == 0 or num % 3 == 0:
    print(f"{num} is divisible by 2 or 3 (or both).")
    if num % 2 == 0:
        print(f"{num} is divisible by 2.")
    if num % 3 == 0:
        print(f"{num} is divisible by 3.")
else:
    print(f"{num} is not divisible by 2 or 3.")
