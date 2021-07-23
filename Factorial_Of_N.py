# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/program-for-factorial-of-a-number/

Program for factorial of a number
Difficulty Level : Basic
Last Updated : 08 Jun, 2021
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

"""

sum1 = 0

def factorial(n):
    if n == 1:
        return  1
    return n  * factorial(n-1)
    
print (factorial(5))
    