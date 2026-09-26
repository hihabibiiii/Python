# Question:
# Take a number from the user and print its multiplication table (1 to 10)
# using a for loop.
#
# Example:
#   Input: 5
#   Output:
#     5 x 1  = 5
#     5 x 2  = 10
#     ...
#     5 x 10 = 50

number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"  {number} x {i:2} = {number * i}")
