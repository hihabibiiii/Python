# Question: Create a Temperature class with celsius attribute and to_fahrenheit() method.
# Ask the user for a temperature in Celsius and convert it.

# Formula: F = (C × 9/5) + 32

# Example output:
# Enter temperature in Celsius: 100
# 100°C = 212.0°F
# 100°C = 373.15 K (Kelvin)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def display(self):
        print(f"{self.celsius}°C = {self.to_fahrenheit():.1f}°F")
        print(f"{self.celsius}°C = {self.to_kelvin():.2f} K (Kelvin)")

# User input
celsius = float(input("Enter temperature in Celsius: "))
temp = Temperature(celsius)
temp.display()

# Show common reference points
print("\n--- Common Reference Points ---")
references = [Temperature(0), Temperature(100), Temperature(-40), Temperature(37)]
for t in references:
    print(f"  {t.celsius:>5}°C → {t.to_fahrenheit():.1f}°F")
