# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:54:48 2019

@author: Anoop K. Jangir
"""

#Challenge 7
#Taking a guess number from the user and random number as secret number.And then ask player to play again the game. 
import random
secret_number=random.randint(1,10)
i=input("Do you want to play again (Y/N)")

while(i!="N"):
    if i=="Y":    
        guess_number=int(input("Enter the number:"))
        if (guess_number==secret_number):
            print("Player wins Computer loses.")
        else:
            print("Computer Wins Player loses.")
        i=input("Do you want to play again (Y/N)")