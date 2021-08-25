# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:31:18 2021

@author: VIP
"""


def viralAdvertising(n):
    import math
    start  =5
    day =1
    while (day<n):
        
        adv = math.floor(start/2)
        total  = adv + start
        start = adv
        day = day +1
        
      
       
    return total     

n=4
print (viralAdvertising(n))
    