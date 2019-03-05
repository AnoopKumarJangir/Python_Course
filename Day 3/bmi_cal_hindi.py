# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:24:37 2019

@author: Anoop K. Jangir
"""

#Take weight and height in killogram and meters 
weight = float(input("किलोग्राम में वजन दर्ज करें: "))
print ("शरीर का वजन:",weight)
height = float(input("मीटर में ऊंचाई दर्ज करें: "))
print("शरीर की ऊंचाई:",height)

#calculate and print BMI
print("बीएमआई है: ", round(weight / (height * height), 2))