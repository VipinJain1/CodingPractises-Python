# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:59:47 2021

@author: VIP
"""

def kangaroo(x1, v1, x2, v2):
    # Write your code here
 
    count  =0
    while (True):
        x1  = x1+v1
        x2 = x2+v2
        if (x1 > x2 and v1 > v2 )  or (x1 < x2 and v1 < v2 )  :
            return "NO"
        
        if count  == 1000:
            return "NO"
        if v1 > v2:
            if x1 > x2:
                return 'NO'
        if x1 == x2:
            return "YES" 
        count = count +1
        
   
x1 = 0
v1= 2 
x2= 5 
v2 = 3

print (kangaroo(x1, v1, x2, v2) )