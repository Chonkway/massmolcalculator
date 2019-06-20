"""A simple molarity calculator to import into ChonkBot under his later 'Tools' section
    Mass (g) = Concentration (mol/L) x Volume (L) x Molecular Weight (g/mol)
        f = Formula(input("Enter the formula of your solution").upper())
"""
import os
from molmass import Formula
import re

print("~~~~~~~~~Please choose what you wish to calculate~~~~~~~~~~")
choice = input(" [1]Molarity" + "\n [2]Moles" + "\n [3]Volume" + "\n [4]Mass <-> Moles").title().strip()
if choice == '1': #If user input is molarity check for moles and volume
    n = input("Enter the moles of solution you have:")
    V = input("Enter your volume in mL or L:")
    if V.endswith('L'):
        n1 = re.sub('[^0-9]','', n)
        V1 = re.sub('[^0-9]','', V)
        molarity = (int(n1)/((int(V1))))
        print("Your molarity is " + str(molarity) + " moles/liter")
    elif V.endswith('mL'):
        n1 = re.sub('[^0-9]','', n)
        V2 = re.sub('[^0-9]','', V)
        molarity = (int^(n)/((int(V)/1000)))
        print("Your molarity is " + str(molarity) + " moles/liter")
    else: #If L or mL is not input the program assumes the volume is in liters
        n1 = re.sub('[^0-9]','', n)
        V1 = re.sub('[^0-9]','', V)
        molarity = (int(n1)/((int(V1))))
        print("Your molarity is " + str(molarity) + " moles/liter")
if choice == '2':
    M = input("Please enter the Molarity of your solution:")
    V = input("Enter your volume in mL or L:")
    if V.endswith('mL'):
        M1 = re.sub('[^0-9]','', M)
        V1 = re.sub('[^0-9]','', V)
        n = (int(M1)*int(V1/1000))
        print("You have " + str(n) + " moles of solution")
    elif V.endswith('L'):
        M1 = re.sub('[^0-9]','', M)
        V1 = re.sub('[^0-9]','', V)
        n = (int(M1)*int(V1))
        print("You have " + str(n) + " moles of solution")
    else:
        M1 = re.sub('[^0-9]','', M)
        V1 = re.sub('[^0-9]','', V)
        n = (int(M1)*int(V1))
        print("You have " + str(n) + " moles of solution")
if choice == '3':#n/M
    n = input("Enter the moles of solution you have:")
    M = input("Please enter the Molarity of your solution:")
    V = (int(n)/int(M))
    print("The volume of solution is " + str(V) + " liters." + "\n In mL this volume is " + str((V/1000)) + " mL.")
if choice == '4':
    option = input("[1]Grams to Moles \n[2]Moles to Grams")
    if option == '1':
        f = Formula(input("Enter the formula of your solution").upper())
        mass = f.mass
        grams = input("How many grams of " + str(f) + " do you have?")
        moles = (int(grams)/int(mass))
        print(str(grams) + " grams of " + str(f) + " is roughly equal to " + str(moles) + "moles of " + str(f))
    elif option == '2':
        f = Formula(input("Enter the formula of your solution").upper())
        mass = f.mass
        moles = input("How many moles of " + str(f) + " do you have?")
        grams = (int(moles)*int(mass))
        print(str(moles) + " moles of " + str(f) + " is roughly equal to " + str(grams) + "grams of " + str(f))
    else:
        exit()
