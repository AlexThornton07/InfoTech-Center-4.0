# Programmer: Alex Thornton
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



