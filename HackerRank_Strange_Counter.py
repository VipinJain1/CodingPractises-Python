# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:13:15 2021

@author: VIP
"""


def strangeCounter(t):
    
    time =1
    start = 3
    value = start
    
    if t <=0:
        return None
    
    while (value >=0):
        
        if time == t:
            return value
        
        if (value == 1):
            value = start *2
            start = value
        else:
            value = value -1
        time  = time +1
                
t =1000000000
print (strangeCounter(t))
    