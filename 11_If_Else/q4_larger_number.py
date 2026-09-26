# Question:
# Take two numbers from the user.
# Print the larger number, or 'Equal' if both numbers are the same.
#
# Example:
#   Input: 10, 5  -> Output: 10 is larger
#   Input: 3, 3   -> Output: Equal

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is larger")
else:
    if num1 == num2:
        print("Equal")
    else:
        print(f"{num2} is larger")
