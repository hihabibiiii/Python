# Question:
# Take a number from the user.
# If it is divisible by both 3 AND 5, print "FizzBuzz".

# Example:
# Enter a number: 15
# FizzBuzz

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
