# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:59:46 2019

@author: Anoop K. Jangir
"""

#Giving the input of first name and last name as according to the string and then print that string in reverse order. 
first = input("Enter the first name:")
last = input("Enter the last name:")
print ("The full name in reverse:{} {}".format(last,first))

#Now finding the space between then and print using slicing of the same string in reverse order. 
name = first+" "+last
print ("The full name:",name)
s = name.index(' ')
print ("The full name after slicing in reverse:",name[s:]+" "+name[:s])