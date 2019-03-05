# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:39:59 2019

@author: Anoop K. Jangir
"""

#Taking a hardcoded string RESTART as into a newstr.
newstr = 'RESTART' 
print (newstr)

#In a hardcoded string RESTART, replacing all the R with $ except the first occurrence and printing the final string.
newstr1 = newstr.replace('R','$')
char = newstr[0]
newstr1 = char + newstr1[1:]
print ("The new string of {}: {}".format(newstr,newstr1))