# Question 4 (Easy):
# Define a function called is_even_or_odd that takes an integer
# and prints whether it is even or odd.

# Solution:
def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Test with several numbers
for n in [0, 1, 4, 7, 100, 999]:
    is_even_or_odd(n)

# Get number from user
num = int(input("\nEnter a number: "))
is_even_or_odd(num)

# Example Input:  13
# Example Output:
# 0 is Even
# 1 is Odd
# ...
# 13 is Odd
