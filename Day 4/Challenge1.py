# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:09:35 2019

@author: Anoop K. Jangir
"""

#Challenge 1
#Importing random module to choose a random value bt the computer itself as save it in name of secret_number.
import random
secret_number=random.randint(0,10)

#Now taking a number by the user from the keboard and store it in the name of guess_number.
guess_number=int(input("Enter your number:"))

#After getting the number then compare them and show who win this guessing game between computer and user. 
if(secret_number == guess_number):
    print("Player Wins And Computer Loses.")
else:
    print("Player Loses And Computer Wins.")