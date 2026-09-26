# Question:
# Create a class Temperature where __init__ takes a value as a string
# (e.g., "37.5") and stores it as a float internally.

class Temperature:
    def __init__(self, value_str):
        self.celsius = float(value_str)  # Convert string to float in constructor

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def __str__(self):
        return f"{self.celsius}°C ({self.to_fahrenheit():.2f}°F)"

t1 = Temperature("37.5")
t2 = Temperature("100")
t3 = Temperature("0")

print(t1)
print(t2)
print(t3)
