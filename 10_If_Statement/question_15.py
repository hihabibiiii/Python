# Question:
# Take a number from the user.
# If it is a perfect square (its integer square root squared equals itself),
# print "Perfect square".

# Example:
# Enter a number: 25
# Perfect square

num = int(input("Enter a number: "))

if num >= 0 and int(num**0.5)**2 == num:
    print("Perfect square")
