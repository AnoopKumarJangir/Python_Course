# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:46:44 2019

@author: Anoop K. Jangir
"""

#Hands on 1
string="Haryana"
#Printing the given string by using even index number.
print(string[1:7:2])

#Hands on 2
string="Haryana"
#Printing the given string reverse order.
print(string[::-1])

#Hands on 3
string="Forsk Technologies"
#Printing the forsk using slicing and indexing is in forward left to right.
print(string[0:5])

#Hands on 4
string="Forsk Technologies"
#Printing the Technologies using slicing and indexng is in forward left to right.
print(string[6:])

#Hands on 5
string="Forsk Technologies"
#Printing Forsk using slicing and inndexing is in Reverse Right to Left.
print(string[-19:-13])

#Hands on 6
string = "Forsk Technologies"
#Printing Technologies using slicing ( forward indexing Right to Left ) 
print(string[-12:])

#Hands on 7
string = "Forsk Technologies"
#Printing ksroF using slicing ( forward indexing Left to Right  ) 
print(string[-14:-19:-1])

#Hands on 8
string = "Forsk Technologies"
#Printing siesgolonhceT using slicing ( forward indexing Left to Right ) 
print(string[-1:-13:-1])

#Hands on 9
string = "Forsk Technologies"
#Printing Technologies Forsk using slicing ( forward indexing Left to Right  )  
print(string[6:18]+" "+string[0:5])

#Hands on 10
string = "Forsk Technologies"
#Printing Technologies Forsk using slicing ( Reverse indexing Right to Left )
print(string[-12:]+" "+string[-20:-13])