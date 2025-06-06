# -*- coding: utf-8 -*-
"""P2Lab2_BranchJerico.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JWb73NQfO0BUX42OVw60UXDtHONCGjXB
"""

#Jerico Branch
#2/18/2025
#P2LAB2
#Using f-strings to display circle calculations

# Create the dictionary with automobile names as keys and their MPG values as values
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the keys in the dictionary
keys = vehicle_mpg.keys()

# Print all the keys
print(keys)

# Prompt the user to enter a vehicle from the dictionary
vehicle = input("Enter one of the vehicles from the list (Camaro, Prius, Model S, Silverado): ")

# Display the mpg for the vehicle entered by the user
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")

    #  Prompt the user to enter the number of miles they will drive
    miles = float(input(f"How many miles will you drive the {vehicle}? "))

    #  Calculate the gallons of gas needed
    gallons_needed = miles / mpg

    #  Determine singular or plural for "gallon(s)"
    gallon_word = "gallon" if gallons_needed == 1 else "gallons"

    # Display the gallons needed
    print(f"{gallons_needed:.2f} {gallon_word}(s) of gas are needed to drive the {vehicle} {miles} miles.")