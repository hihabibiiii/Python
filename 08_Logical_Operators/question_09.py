# Question:
# Take three numbers from the user.
# Check if all three are positive using `and`.

# Example:
# Enter first number: 3
# Enter second number: 7
# Enter third number: -1
# Not all numbers are positive.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > 0 and b > 0 and c > 0:
    print("All three numbers are positive.")
else:
    print("Not all numbers are positive.")
