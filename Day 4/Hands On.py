# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:35:09 2019

@author: Anoop K. Jangir
"""

# Hands On  1
# Printing all the numbers from 1 to 10 using condition in while loop.
n = 1 
while(n <= 10):
    print(n)
    n=n+1
    
# Hands On  2
#  Printing all the numbers from 1 to 10 using while True loop.
n = 1
while (True):
    print (n)
    n = n+1
    if(n == 11):
        break
    
# Hands On 3
#  Printing all the even numbers from 1 to 10 using condition in while loop.
n = 1
while (n<=10):
    if(n%2==0):
        print(n)
    n=n+1
    
# Hands On 4
#  Printing all the even numbers from 1 to 10 using while True loop.
n=1
while(True):
    if(n%2==0):
        print(n)
        if(n==10):
            break
    n=n+1
    
# Hands On 5
#  Printing all the odd numbers from 1 to 10 using condition in while loop.
n=1
while(n<=10):
    if(n%2 != 0):
        print(n)
    n=n+1

# Hands On 6
#  Printing all the odd numbers from 1 to 10 using while True loop.  
n=0
while(True):
    if(n%2 != 0):
        print(n)
    elif(n==10):
        break
    n=n+1
    
# Hands On 7
#  Printing all the prime numbers from 1 to 10 using condition in while loop.
n=1
while(n<=10):
    if(n>1):
        if(n*1 == n and n%n == n):
            print(n)
    n=n+1

# Hands On 8
#  Printing all the prime numbers from 1 to 10 using while True loop.
n=1
while(True):
    if(n>1):
        print(n)
    n=n+1
    if(n==11):
        break