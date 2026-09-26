# Question 5 (Easy):
# Take two numbers from the user.
# Compute and print both the floor division result (//) and the modulo (remainder %).

# Solution:
num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor : "))

floor_div = num1 // num2
remainder = num1 % num2

print(f"{num1} // {num2} = {floor_div}  (floor division)")
print(f"{num1} %  {num2} = {remainder}  (remainder)")

# Example:
# 17 // 5 = 3
# 17 %  5 = 2
