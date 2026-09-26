# Question:
# Simulate a menu-driven unit converter using if/elif/else.
# Show the user this menu:
#   1 = Kilometers to Miles
#   2 = Kilograms to Pounds
#   3 = Celsius to Fahrenheit
#   4 = Liters to Gallons
# Ask for the choice and the value, then print the converted result.
#
# Conversion factors:
#   1 km  = 0.621371 miles
#   1 kg  = 2.20462 pounds
#   C to F: F = (C * 9/5) + 32
#   1 L   = 0.264172 gallons
#
# Example:
#   Choice: 1, Value: 10  -> Output: 10 km = 6.21 miles

print("=== Unit Converter ===")
print("1 = Kilometers to Miles")
print("2 = Kilograms to Pounds")
print("3 = Celsius to Fahrenheit")
print("4 = Liters to Gallons")

choice = input("\nEnter your choice (1-4): ")
value = float(input("Enter the value to convert: "))

if choice == "1":
    result = value * 0.621371
    print(f"{value} km = {result:.4f} miles")
elif choice == "2":
    result = value * 2.20462
    print(f"{value} kg = {result:.4f} pounds")
elif choice == "3":
    result = (value * 9 / 5) + 32
    print(f"{value} °C = {result:.2f} °F")
elif choice == "4":
    result = value * 0.264172
    print(f"{value} liters = {result:.4f} gallons")
else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
