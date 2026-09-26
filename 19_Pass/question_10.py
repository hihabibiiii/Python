# Question:
# Use `pass` in a nested if where one branch is not yet implemented.
# Classify a number: positive even, positive odd, or non-positive.
# The non-positive branch uses pass (not implemented).

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    pass  # TODO: handle non-positive numbers later
    print("(Non-positive handling not yet implemented.)")
