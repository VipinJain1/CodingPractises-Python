# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP
"""

sum1 = 0
def recSum(n):
    if n ==0:
        return  0
    return n + recSum(n-1)
    
print (recSum(20))
    