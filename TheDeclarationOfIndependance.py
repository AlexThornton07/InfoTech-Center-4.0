# Programmer: Alex thornton
# Date Merged: 2.6.2023
# Merged Welcome Screen and Gasoline Branches - Stable

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import Libraries Hear
import time
import sys
import random
from time import sleep


print("\n\n\033[1;44;40mWelcome - InfoTechCenter 4.0 ")

x = 0
a = 0

timeToSleep = 2
print('')

while x != 20:
    x += 1
    b = ("\033[1;44;40mInfoTechCenter 4.0 OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40mMission Accomplished - Retina Scanned - Access Granted\n')

# Programmer: Alex Thornton
# Date: 1.30.23
# Program: InfoTech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge Level
  -Create a List with Gas Levels
  -Randomize and choose from the list to determine our gas level

Create a Function to determine our closest Gas Station
  -Create a List of gas stations
  -Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
  -Print Gas Level
  -Print Gas Station
"""



# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations Function
def listOfGasStations():
  gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon"]
  gasStationNearby = random.choice(gasStations)
  return gasStationNearby

# Determine Gas Level & Closest Gas Station

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE RUNNING ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is low, searching Google Maps for nearby Gas Stations")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is",listOfGasStations(),"which is",milesToGasStationQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full which is a plenty of gas to make it to your destinations today")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank which is plenty of gas to make it to your destination today")
    else:
        print("Your gas tank is full - Hooray!!!")



# Programmer: Alex Thornton
# Date: 2.8.23
# Program: Weather System Updates 

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


#Call Functions Here
vehicleResponseSystem()
gasLevelAlert()