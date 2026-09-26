# Question 15 (Hard):
# Compute BMI (Body Mass Index).
# Formula: BMI = weight (kg) / height (m) ** 2
# Take weight and height from the user.
# Print the BMI and category: Underweight (<18.5), Normal (18.5-24.9),
# Overweight (25-29.9), Obese (>=30).

# Solution:
weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in m  : "))

bmi = weight / height ** 2

print(f"\nWeight : {weight} kg")
print(f"Height : {height} m")
print(f"BMI    : {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")

# Example:
# Weight: 70 kg, Height: 1.75 m
# BMI = 70 / 1.75^2 = 22.86 -> Normal weight
