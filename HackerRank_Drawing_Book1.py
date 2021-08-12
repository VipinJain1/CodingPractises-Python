# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:27:06 2021

@author: VIP
"""


def pageCount(n, p):
    # Write your code here
     
    if p ==0 or n ==0:
        return 0
    
    if n-p <=2  or p <=1:
        return 0
        
    a = int((n-p)/2)
    b = int (p/2)
    return min(a,b)

        

n =5
p =4
print (pageCount(n,p))