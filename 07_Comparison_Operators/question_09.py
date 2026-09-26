# Question 9 (Medium):
# Take a temperature from the user.
# Compare it to thresholds and print the condition:
#   < 0  : Freezing
#   0-15 : Cold
#   16-30: Mild
#   > 30 : Hot

# Solution:
temp = float(input("Enter temperature (°C): "))

if temp < 0:
    condition = "Freezing"
elif temp <= 15:
    condition = "Cold"
elif temp <= 30:
    condition = "Mild"
else:
    condition = "Hot"

print(f"{temp}°C -> {condition}")

# Example:
# -5  -> Freezing
# 10  -> Cold
# 22  -> Mild
# 35  -> Hot
