# Question:
# Take a number from the user and check if it is a palindrome using a while loop.
# A number is a palindrome if it reads the same forwards and backwards.
# (Reverse the number and compare it to the original.)
#
# Example:
#   Input: 121   -> Output: Palindrome
#   Input: 12321 -> Output: Palindrome
#   Input: 1234  -> Output: Not a palindrome

number = int(input("Enter a positive integer: "))
original = number

reversed_number = 0
temp = number
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp = temp // 10

if original == reversed_number:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is NOT a palindrome")
