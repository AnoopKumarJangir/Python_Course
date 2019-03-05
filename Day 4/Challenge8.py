# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:13:17 2019

@author: Anoop K. Jangir
"""

#Challenge 8
#Importing random module to choose a random value bt the computer itself as save it in name of secret_number.
import random
secret_number=random.randint(0,10)

#Now taking a number by the user from the keboard and store it in the name of guess_number.
#After taking guess and secret number then catches the non integer value when user type in the guess number.
while(True):
    guess_number=input("Enter your number:")
    dt = type(guess_number)
    if(dt != int):
        print("Type integer value.")
    else:
        if(guess_number == secret_number):
            print("Player Wins.")
            break
        else:
            print("Player loses.")