# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:39:05 2019

@author: Anoop K. Jangir
"""

#My present height is 5 foot and 11 inch
foot = 5
inch = 11
print (foot,inch)

#Converting Foot in meters
new_foot = foot * 0.3048
print (new_foot)

#Converting Inch in meters
new_inch = inch *  0.0254
print (str(new_inch))

#Print height in meters
print (new_foot,new_inch)

#Print Height in Centimeters
new_cent_foot = new_foot * 100
print (new_cent_foot)
new_cent_inch = new_inch * 100
print(new_cent_inch)
print (new_cent_foot,new_cent_inch)