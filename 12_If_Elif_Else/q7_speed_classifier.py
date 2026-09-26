# Question:
# Take the speed of a car in km/h from the user.
# Classify the speed as:
#   Slow      -> speed < 40
#   Normal    -> 40 <= speed <= 80
#   Fast      -> 81 <= speed <= 120
#   Dangerous -> speed > 120
#
# Example:
#   Input: 30   -> Output: Slow
#   Input: 60   -> Output: Normal
#   Input: 100  -> Output: Fast
#   Input: 150  -> Output: Dangerous

speed = float(input("Enter the car speed (km/h): "))

if speed < 40:
    print("Speed category: Slow")
elif speed <= 80:
    print("Speed category: Normal")
elif speed <= 120:
    print("Speed category: Fast")
else:
    print("Speed category: Dangerous")
