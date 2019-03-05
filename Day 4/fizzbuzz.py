# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:52:57 2019

@author: Anoop K. Jangir
"""

#Printing integers from 1 to 100(included). In ehich multiples of three print "Fizz" and the multiples of five print "Buzz" and multiples of both three and five print "FizzBuzz". 
n=1
while(n<=100):
    if(n%3==0):
        if(n%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(n%5==0):
        if(n%3==0):
            print("FizzBuzz")
        else:
            print('Buzz')
    else:
        print(n)
    n=n+1