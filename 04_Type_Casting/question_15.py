# Question 15 (Hard):
# Take a decimal number (float) from the user.
# Cast it to int (truncation).
# Show the difference between the float and the int.
# Compute and print the fractional part that was lost.

# Solution:
float_num = float(input("Enter a decimal number: "))
int_num = int(float_num)
fractional_lost = float_num - int_num

print(f"\nOriginal float : {float_num}")
print(f"After int cast : {int_num}")
print(f"Difference     : {float_num} - {int_num} = {fractional_lost:.6f}")
print(f"Fractional part lost: {fractional_lost:.6f}")

# Example Input / Output:
# Enter a decimal number: 9.75
# Original float : 9.75
# After int cast : 9
# Difference     : 9.75 - 9 = 0.750000
# Fractional part lost: 0.750000
