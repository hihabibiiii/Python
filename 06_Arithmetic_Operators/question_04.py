# Question 4 (Easy):
# Take two numbers from the user and print their quotient (float division).

# Solution:
num1 = float(input("Enter dividend: "))
num2 = float(input("Enter divisor : "))

if num2 != 0:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Error: Cannot divide by zero.")

# Example: 10 / 4 = 2.5
