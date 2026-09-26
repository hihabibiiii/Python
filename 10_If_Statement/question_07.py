# Question:
# Take three numbers from the user.
# If all three numbers are equal, print "All numbers are equal".

# Example:
# Enter first number: 7
# Enter second number: 7
# Enter third number: 7
# All numbers are equal

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All numbers are equal")
