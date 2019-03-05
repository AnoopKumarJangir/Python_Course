# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:48:30 2019

@author: Anoop K. Jangir
"""

#Taking the input string as according to the given paragraph in a variable.
string ="""This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes."""

#Printing the given string only the last line by using indexing.
s = string.index('F')    
print (string[s:])