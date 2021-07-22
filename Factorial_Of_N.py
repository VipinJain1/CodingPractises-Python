# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP
"""

sum1 = 0

def factorial(n):
    if n == 1:
        return  1
    return n  * factorial(n-1)
    
print (factorial(5))
    