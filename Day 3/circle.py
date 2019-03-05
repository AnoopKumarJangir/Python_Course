# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:58:52 2019

@author: Anoop K. Jangir
"""

#Importing the Module math by using import. After getting the module finding the function of Pi and taking some help.
import math
dir (math)
help (math.pi)

#Taking the radius of the circle by the user.
radius = float(input("Enter the radius of the circle:"))
print (radius)

#Now solving the area and then print the area of the circle by using pi and rdius.
from math import pi as Pi
area = str(Pi * radius * radius)
print ("The Area of the circle of radius {}: {}".format(radius,area))

#Then solving perimeter of the same circle by using the pi and radius and also printing the perimeter.
from math import pi as Pi
perimeter = str(2 * Pi * radius)
print ("The Perimeter of the circle of radius {}: {}".format(radius,perimeter))