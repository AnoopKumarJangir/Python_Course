# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:23:09 2019

@author: Anoop K. Jangir
"""

#Taking the name as an input by the keyboard as like name or any string.
newstr = input("Enter the word:")
print (newstr)

#Now firstly printing the word into upper case letters and print it.
newstr1 = newstr.upper()
print ("The uppercase letter of the word {}: {}".format(newstr,newstr1))

#Now printing the word into lower case letters and print it.
newstr2 = newstr.lower()
print ("The lowercase letter of the word {}: {}".format(newstr,newstr2))

#Now printing the word into camelcase or titlecase letters and print it.
newstr3 = newstr.title()
print ("The camelcase letter of the word {}: {}".format(newstr,newstr3))