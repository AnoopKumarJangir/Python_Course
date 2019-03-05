# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:55:45 2019

@author: Anoop K. Jangir
"""

#Calculate and print ponderal index
weight = float(input("Weight in kilogram: "))
print (weight)
height = float(input("Height in meters: "))
print(height)
BMI = round(weight / (height * height), 2)
print ("BMI is: ", BMI)
print ("PI is: ",(BMI/weight))