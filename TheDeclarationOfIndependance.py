# Programmer: Alex Thornton
# Date: 2.8.23
# Program: Weather System Updates 

# Import Libraries Here
import random

# Create weather condition in a list and choose it randomly

def weather():
    weatherForcast = ["Snowing","Blizzard","Rain","Windy","Foggy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()

# VRS() to respond to the weather condition 
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forcast of",weatherAlert)
        print("VRS has been engaged only allowing your vehicle only to go 45mph")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of a",weatherAlert)
        print("VRS has been engaged only allowing your vehicle only to go 35mph")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for",weatherAlert,"plesed drive carefully")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your alarm by 60 minutes because of",weatherAlert,"weather, please drive carefully")
        print("VRS has been engaged only allowing your vehicle only to go 30mph")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully")
    else:
         print("\nNWS is calling for",weatherAlert,"have a safe and wonderful day!")

vehicleResponseSystem()