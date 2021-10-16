# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:33:03 2021

@author: VIP
"""
# Wrong

a =[2,1,5,6,2,3,7,5,3,4,5,76,7,8,98,9]

import heapq
heapq.heapify (a)

area  =0 
for  data in  heapq.nsmallest (len (set(a)),set (a)):
    
    d = [i for i in a if i >=data]
    ln = len(d)
    if area < ln *data:
        area = ln*data

print (area)
    
    
