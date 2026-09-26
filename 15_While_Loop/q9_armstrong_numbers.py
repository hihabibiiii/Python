# Question:
# Print all Armstrong numbers between 1 and 500 using a while loop.
# An Armstrong number (narcissistic number) is a number that equals
# the sum of its own digits each raised to the power of the number of digits.
# Examples: 1, 2, ..., 9 (1-digit), 153 (1^3+5^3+3^3=153), 370, 371, 407
#
# Expected Output:
#   Armstrong numbers between 1 and 500:
#   1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407

print("Armstrong numbers between 1 and 500:")
armstrong_list = []

num = 1
while num <= 500:
    # Determine number of digits
    digits = len(str(num))
    # Sum of digits raised to the power
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10
    if total == num:
        armstrong_list.append(num)
    num = num + 1

print(", ".join(str(n) for n in armstrong_list))
