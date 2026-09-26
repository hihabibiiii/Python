# Question:
# Use @property and @property.setter decorators together.
# Property with getter AND setter.

class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

t = Temperature(25)
print(f"Celsius:    {t.celsius}°C")
print(f"Fahrenheit: {t.fahrenheit}°F")

# Set via property setter
t.celsius = 100
print(f"\nUpdated: {t.celsius}°C = {t.fahrenheit}°F")

# Invalid value
try:
    t.celsius = -300
except ValueError as e:
    print(f"Error: {e}")
