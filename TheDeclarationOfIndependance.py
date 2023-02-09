# Programmer: Alex Thornton
# Date: 2.8.23
# Program: Weather System Updates 

# Import Libraries Here
import random

# Create weather condition in a list and choose it randomly

def weather():
    weatherForcast = ["Snowing","Blizzard","Raining","Windy","Foggy","Icy","Sunny"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()

print(weatherAlert)

# VRS() to respond to the weather condition 
def vehicleResponseSystem():
    print("Howdy")