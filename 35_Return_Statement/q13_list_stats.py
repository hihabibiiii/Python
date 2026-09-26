# Question 13 (Hard):
# Define a function called list_stats that takes a list of numbers
# and returns a TUPLE of (minimum, maximum, total_sum, average).
# Unpack and display all four statistics.

# Solution:
def list_stats(numbers):
    if not numbers:
        return None  # handle empty list

    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num

    average = total / len(numbers)
    return minimum, maximum, total, average

# Test
data = [12, 5, 38, 7, 22, 1, 45, 9, 17, 30]
print("Data:", data)

mn, mx, sm, avg = list_stats(data)
print(f"\nMinimum:  {mn}")
print(f"Maximum:  {mx}")
print(f"Sum:      {sm}")
print(f"Average:  {avg:.2f}")

# Get numbers from user
raw = input("\nEnter numbers separated by spaces: ")
user_data = [float(x) for x in raw.split()]
mn2, mx2, sm2, avg2 = list_stats(user_data)
print(f"Min={mn2}, Max={mx2}, Sum={sm2}, Avg={avg2:.2f}")

# Example Input:  4 8 15 16 23 42
# Example Output: Min=4.0, Max=42.0, Sum=108.0, Avg=18.00
