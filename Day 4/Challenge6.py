# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:49:18 2019

@author: Anoop K. Jangir
"""

#Challenge 6
#Importing random module to choose a random value bt the computer itself as save it in name of secret_number.
import random
secret_number=random.randint(0,10)

#Now taking a number by the user from the keboard and store it in the name of guess_number.
guess_number=int(input("Enter your number:"))
n = 1
print("Number of tries left:",6-n)
  
#After getting the number then compare them and show who win this guessing game between computer and user till the user can't get the secret number at 6 times. 
while (n<6):
    n=n+1
    if(guess_number != secret_number):
        guess_number = int(input("Enter the number:"))
        print("Number of tries left:",6-n)

    else:
        print("Player Wins.")
        print("The Secret number:",secret_number)
        break
  
