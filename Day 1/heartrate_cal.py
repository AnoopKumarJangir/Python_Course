# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:41:36 2019

@author: Anoop K. Jangir
"""

#Assume my age 21
my_age = 21
print (my_age)

#Calculate maximum heart rate
max_hr = 220 - my_age
print (max_hr)

#calculate target heart rate
low_hr = max_hr * 0.70
print (low_hr)
high_hr = max_hr * 0.85
print (high_hr)

#calculate heart rate bites per minute
print ("Heart rate is" + str(low_hr) +   "  to  "   + str(high_hr) + " beates per minute.")