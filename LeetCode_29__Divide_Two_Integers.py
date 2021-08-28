# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:19:41 2021

@author: VIP
"""

def divide(dividend, divisor):
    count =0
    mins =0
      
    if (dividend == -1  and  divisor ==1 ) or  (dividend == 1  and  divisor == -1 ) :
        return -1
    
    if dividend == divisor:
        return 1
    
    if divisor ==1  and dividend >0:
        return dividend
    
    if divisor ==1  and dividend <0:
        return -dividend
    
    if divisor == -1 and dividend >0:
        return -dividend
        
    if divisor == -1 and dividend <0: 
        return abs (dividend)
        
    if divisor < 0:
        mins = 1
        divisor = abs (divisor)
    if dividend < 0:
        mins = 1
        dividend = abs (dividend)
    
    while (dividend-divisor>0 ):
        dividend   = dividend -divisor
        count +=1
    
    if (mins ==1):
        
        return -count
    else:
        return count
    

dividend = -2124455676777
divisor = -1
print (divide(dividend,divisor))