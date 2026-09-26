# Question:
# Create a lambda function that converts Celsius to Fahrenheit.
# Formula: F = (C * 9/5) + 32

celsius_to_f = lambda c: (c * 9 / 5) + 32

print(f"0°C   = {celsius_to_f(0)}°F")
print(f"100°C = {celsius_to_f(100)}°F")
print(f"37°C  = {celsius_to_f(37):.2f}°F")
