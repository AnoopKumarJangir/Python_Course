# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:02:36 2019

@author: Anoop K. Jangir
"""

#Take weight and height in killogram and meters 
body_weight = float(input("Weight in kilogram: "))
print (body_weight)
body_height = float(input("Height in meters: "))
print(body_height)

#calculate and print BMI
print("BMI is: ", round(body_weight / (body_height * body_height), 2))