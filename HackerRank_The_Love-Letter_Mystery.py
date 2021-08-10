# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:48:36 2021

@author: VIP
"""

def theLoveLetterMystery(s):
    # Write your code here
    count  =0
    
    if s == reversed (s):
        return 0
    
    
    for i in range (0,len (s)):
        num = ord (s[i])  -97
        if num >0:
            orig = s[i]
            count  = count +1
            ch = chr(num -1)
            s[i] = ch
            
            if (s == revrsed(s)):
                return count
            else:
                s[i] = orig
                
            
            
             
        



s ='abc'

result = theLoveLetterMystery(s)
