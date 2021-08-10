# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:07:06 2021

@author: VIP
"""

from  collections import Counter

def migratoryBirds(arr):
    d = Counter (arr)
    val =  max(d.values())
    l = []
    for i, val1 in d.items():
        
        if  val1 == val:
            
            l.append (i)
    
    return min (l)
        
    
    
arr = [1,4,4,5,5,3]
print (migratoryBirds(arr))