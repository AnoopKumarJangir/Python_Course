# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:25:28 2019

@author: Anoop K. Jangir
"""

#Importing the Module math by using import. After getting the module finding the function of Factorial and taking some help. 
import math
dir ( math )
help (math.factorial)

#Taking th input from the user by using the keyboard in the variable of number.
number = input("Enter the number=")
print(number)

#Now solving factorial of the number and then print the factorial.
from math import factorial
fact = factorial(int( number ))
print (fact)
print ("Factorial of {} : {}".format( number,fact))