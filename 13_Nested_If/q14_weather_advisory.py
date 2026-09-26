# Question:
# Give a weather advisory using nested if based on temperature, wind, rain, and humidity.
# Rules:
#   If temp < 0:
#       If wind > 30: 'Dangerous wind chill! Stay indoors.'
#       Else: 'Cold weather. Dress warmly.'
#   If 0 <= temp <= 15:
#       If raining == 'yes': 'Cool and rainy. Carry an umbrella.'
#       Else: 'Cool weather. A light jacket recommended.'
#   If temp > 35:
#       If humidity > 80: 'Heat index warning! Risk of heat stroke.'
#       Else: 'Hot weather. Stay hydrated.'
#
# Example:
#   temp=-5, wind=40  -> Dangerous wind chill!
#   temp=10, rain=yes -> Cool and rainy. Carry an umbrella.
#   temp=38, hum=85   -> Heat index warning!

temp = float(input("Enter temperature (°C): "))

if temp < 0:
    wind = float(input("Enter wind speed (km/h): "))
    if wind > 30:
        print("Dangerous wind chill! Stay indoors.")
    else:
        print("Cold weather. Dress warmly.")
else:
    if temp <= 15:
        raining = input("Is it raining? (yes/no): ").lower()
        if raining == "yes":
            print("Cool and rainy. Carry an umbrella.")
        else:
            print("Cool weather. A light jacket recommended.")
    else:
        if temp > 35:
            humidity = float(input("Enter humidity (%): "))
            if humidity > 80:
                print("Heat index warning! Risk of heat stroke. Stay cool.")
            else:
                print("Hot weather. Stay hydrated and seek shade.")
        else:
            print("Pleasant weather. Enjoy your day!")
