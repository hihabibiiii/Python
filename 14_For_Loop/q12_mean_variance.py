# Question:
# Take 5 numbers from the user using a for loop.
# Compute and print:
#   1. The mean (average)
#   2. The variance (average of squared differences from the mean)
#
# Formula:
#   mean     = sum(numbers) / count
#   variance = sum((x - mean)^2 for each x) / count
#
# Example:
#   Numbers: 2, 4, 4, 4, 5, 5, 7, 9  (using 5 here: 2, 4, 4, 4, 5)
#   Mean = 3.8, Variance = 0.96

numbers = []
print("Enter 5 numbers:")
for i in range(1, 6):
    num = float(input(f"  Number {i}: "))
    numbers.append(num)

# Compute mean
total = 0
for num in numbers:
    total = total + num
mean = total / 5

# Compute variance
sum_sq_diff = 0
for num in numbers:
    diff = num - mean
    sum_sq_diff = sum_sq_diff + (diff * diff)
variance = sum_sq_diff / 5

print(f"\nNumbers : {numbers}")
print(f"Mean     : {mean:.4f}")
print(f"Variance : {variance:.4f}")
