# Question:
# Create a Temperature class that stores internally in Celsius.
# Expose Fahrenheit and Kelvin via @property.

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @property
    def kelvin(self):
        return self.__celsius + 273.15

    def __str__(self):
        return (f"Temperature: {self.__celsius:.2f}°C | "
                f"{self.fahrenheit:.2f}°F | {self.kelvin:.2f}K")

temps = [Temperature(0), Temperature(100), Temperature(37), Temperature(-40)]
for t in temps:
    print(t)
