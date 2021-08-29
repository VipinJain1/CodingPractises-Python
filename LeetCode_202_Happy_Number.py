# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:47:01 2021

@author: VIP
"""

def isHappy(n):
    if n ==0:
        return False
    
    if n ==1:
        return True 
    
    if n*n <=9:
        return False
    count =0
    orignum = n
    while (n):
        sm =0
        for i in str(n):
            sm  = sm + int (i) * int (i)
        n = sm
        
        if n==1:
            return True
        if n*n <=9:
            return False
        count = count +1
        
        if count >5 and n == orignum:
            return False
        if count ==1000:
            return False 
            
    
n =5
print (isHappy(n))
