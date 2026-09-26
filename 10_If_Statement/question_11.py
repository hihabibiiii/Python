# Question:
# Take a 4-digit number from the user.
# If the sum of its digits equals 10, print "Digit sum is 10".

# Example:
# Enter a 4-digit number: 1234  (1+2+3+4=10)
# Digit sum is 10

num = int(input("Enter a 4-digit number: "))

d1 = num // 1000
d2 = (num % 1000) // 100
d3 = (num % 100) // 10
d4 = num % 10

if d1 + d2 + d3 + d4 == 10:
    print("Digit sum is 10")
