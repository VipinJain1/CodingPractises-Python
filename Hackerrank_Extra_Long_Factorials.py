# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:54:01 2021

@author: VIP
"""

n =25

def extraLongFactorials(n):
    # Write your code here
     if n ==0 or n ==1:
        return 1 
     return n * extraLongFactorials(n-1)
 
    
 
    
print (extraLongFactorials(25))