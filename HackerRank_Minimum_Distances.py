# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:07:06 2021

@author: VIP
"""

from  collections import Counter


def minimumDistances(a):
    
    l  = len(a)
    
    minDist = l
    found = False
    for i in range (l):
        for  j in range (i+1, l):
            
            if a[i] == a[j]:
                found = True
                dist = abs (i-j)
                if dist < minDist:
                    minDist = dist
                
    if found == False:
        return -1
    else:
        return minDist
    
    
arr = [3,2,1,2,3]
arr = [1,2,3,45]
print (minimumDistances(arr))