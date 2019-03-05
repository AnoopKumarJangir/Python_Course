# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:47:34 2019

@author: Anoop K. Jangir
"""

#Assume that you travel 80 km to office
travel = 80*2
print ("Travelling to office : ",travel)

#Cost of diesel
diesel = 80
print ("Diesel per litre cost : ",diesel)

#Average of vehicle
average = 18
print ("Average of vehicle in km/litres : ",average)

#Cost of the ride
my_car_kilo = travel/average
print (my_car_kilo)

cost = my_car_kilo * diesel
print ("Cost : ",cost)