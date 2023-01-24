# Programmer: Alex Thornton
# Date: 1.20.23
# Program: InfoTech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import Libraries Hear
import time
import sys

print("\n\nWelcome - InfoTechCenter 4.0 ")

x = 0
a = 0

timeToSleep = 2
print('')

while x != 20:
    x += 1
    b = ("\033[1;44;40m InfoTechCenter 4.0 OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')





