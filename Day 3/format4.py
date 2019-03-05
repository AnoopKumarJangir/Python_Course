# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:02:10 2019

@author: Anoop K. Jangir
"""

#Taking the input of first name and last name in a single line code and print full name.
dir (str)
help ('__class__')
first,last = input("Enter the first name:"),input("Enter the last name:")
name = first+" "+last
print ("The full name:",name)

#Printing the full name in reverse order to show with the help of space between them.
print ("The full name in reverse:{} {}".format(last,first))