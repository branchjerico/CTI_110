#Jerico Branch
#2/18/2025
#P2LAB1
#Using f-strings to display circle calculations

import math

#Get the radius from the user
radius = float(input("What is the radius of the circle? "))

#Calculations
diameter = 2 * radius

circumference = 2 * math.pi * radius 

area = math.pi * radius ** 2

print()

#Display all calculations to the user

print(f"The diameter of a circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the cirlce is {area:.3f}")