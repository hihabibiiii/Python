# Question:
# Ask the user for a temperature value and their conversion choice:
#   1 = Celsius to Fahrenheit
#   2 = Fahrenheit to Celsius
# Perform the conversion and print the result.
#
# Formulas:
#   C to F: F = (C * 9/5) + 32
#   F to C: C = (F - 32) * 5/9
#
# Example:
#   Input: 100, choice 1  -> Output: 212.0 °F
#   Input: 32, choice 2   -> Output: 0.0 °C

temperature = float(input("Enter the temperature value: "))
print("1 = Celsius to Fahrenheit")
print("2 = Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature} °C = {fahrenheit:.2f} °F")
else:
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature} °F = {celsius:.2f} °C")
