# Question:
# Take a BMI (Body Mass Index) value from the user.
# Print the BMI category:
#   Underweight  -> BMI < 18.5
#   Normal       -> 18.5 <= BMI <= 24.9
#   Overweight   -> 25 <= BMI <= 29.9
#   Obese        -> BMI >= 30
#
# Example:
#   Input: 17.0  -> Output: Underweight
#   Input: 22.5  -> Output: Normal
#   Input: 27.0  -> Output: Overweight
#   Input: 35.0  -> Output: Obese

bmi = float(input("Enter your BMI value: "))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi <= 24.9:
    print("Category: Normal")
elif bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
