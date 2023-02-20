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
        print("\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***Warning***")
        sleep(1)
        print("\nYour gas tank is low, searching Google Maps for nearby Gas Stations")
        sleep(1)
        print("\nThe closest gas station is",listOfGasStations(),"which is",milesToGasStationLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("\nYour gas tank is at a Quarter Tank and the closest gas station is",listOfGasStations(),"which is",milesToGasStationQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("\nYour gas tank is a half of a tank full which is a plenty of gas to make it to your destinations today")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("\nYour gas tank is at three quarters of a tank which is plenty of gas to make it to your destination today")
    else:
        print("\nYour gas tank is full - Hooray!!!")



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
        print("\nVRS has been engaged only allowing your vehicle only to go 45mph\n")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of a",weatherAlert)
        print("\nVRS has been engaged only allowing your vehicle only to go 35mph\n")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for",weatherAlert,"plesed drive carefully\n")
    elif weatherAlert == "Foggy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully\n")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your alarm by 60 minutes because of",weatherAlert,"weather, please drive carefully\n")
        print("\nVRS has been engaged only allowing your vehicle only to go 30mph\n")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully\n")
    else:
         print("\nNWS is calling for",weatherAlert,"have a safe and wonderful day!\n")


#Call Functions Here
print("\nNational Weather Service is checking conditions...\n")
sleep(1)
vehicleResponseSystem()
print("\nChecking current gas levels...\n")
sleep(1)
gasLevelAlert()


# Date: 1.20.23
# Program: Infotech Center Uprgrades

"""
I will be creating a system that adjusts to the drivers preferences 
"""

#Import Libraries Here:
import random

def Drivers():
    listOfDrivers = ["Driver 1","Driver 2","Driver 3","Driver 4"]
    chooseDriver = random.choice(listOfDrivers)
    return chooseDriver

driverAlert = Drivers()

def Radio():
    listOfRadioStations = ["Rock","Pop","Hip Hop","Country","Top Hits"]
    chooseRadioStation = random.choice(listOfRadioStations)
    return chooseRadioStation

radioAlert = Radio()

def SteeringWheel():
    listOfSteeringWheelPostions = ["Low","Medium","High"]
    chooseSteeringWheelPostion = random.choice(listOfSteeringWheelPostions)
    return chooseSteeringWheelPostion

steeringWheelAlert = SteeringWheel()

def Seat():
    listOfSeatSettings = ["Close","Middle","Far"]
    chooseSeatSetting = random.choice(listOfSeatSettings)
    return chooseSeatSetting

seatAlert = Seat()

#Show Driver Settings

def driverSettings():
    if driverAlert == "Driver 1":
        print("\nDriver 1 has been chosen")
    elif driverAlert == "Driver 2":
        print("\nDriver 2 has been chosen")
    elif driverAlert == "Driver 3":
        print("\nDriver 3 has been chosen")
    else:
        print("\nDriver 4 has been chosen")
driverSettings()

def radioSettings():
    if radioAlert == "Rock":
        print("\nTurning on rock")
    elif radioAlert == "Pop":
        print("\nTurning on pop")
    elif radioAlert == "Hip Hop":
        print("\nturning on hip hop")
    elif radioAlert == "Counrty":
        print("\nturning on country")
    else:
        print("\nturning on top hits")
radioSettings()

def steeringWheelSettings():
    if steeringWheelAlert == "Low":
        print("\nYour steering wheel setting has been changed to low")
    elif steeringWheelAlert == "Medium":
        print("\nYour steering wheel setting has been changed to medium")
    else:
        print("\nYour steering wheel setting has been chnaged to high")
steeringWheelSettings()

def seatSettings():
    if seatAlert == "Close":
        print("\nYour seat postion had been changed to close")
    elif seatAlert == "Middle":
        print("\nYour seat postion has been changed to middle")
    else:
        print("\nYour seat postion has been changed to far")
seatSettings()


vehicleResponseSystem()

# VRS changes the in car temperature depending on weather condition
def temperatureInCar():
    if weatherAlert == "Snowing":
        print("\nThe heat has changed to high and butt warmers are engaged because of",weatherAlert)
    elif weatherAlert == "Blizzard":
        print("\nThe heat has changed to medium and butt warmers are engaged because of",weatherAlert)
    elif weatherAlert == "Rain":
        print("")
    elif weatherAlert == "Windy":
        print("")
    elif weatherAlert == "Icy":
        print("\nDefrost has been engaged and heat has been changed to medium")
    elif weatherAlert == "Foggy":
        print("Headlights have been engaged")
    else:
        print("\nAir Conditioning has been turned on due to",weatherAlert)

temperatureInCar()

