# Question 5 (Easy):
# Define a function called celsius_to_fahrenheit that takes a temperature
# in Celsius and returns the equivalent temperature in Fahrenheit.
# Formula: F = (C * 9/5) + 32

# Solution:
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Test with known values
test_values = [0, 100, -40, 37]
print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)
for c in test_values:
    f = celsius_to_fahrenheit(c)
    print(f"{c:>10} | {f:>12.2f}")

# Get temperature from user
temp_c = float(input("\nEnter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.2f}°F")

# Example Input:  25
# Example Output: 25.0°C = 77.00°F
