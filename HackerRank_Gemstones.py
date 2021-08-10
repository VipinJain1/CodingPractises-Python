# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:36:01 2021

@author: VIP
"""

def gemstones(arr):
    
    d  = dict()
    s = []
    
    for i in arr:
        s.append ( set(i))

    for i in s:
        for j  in i:
            if j not in d.keys():
                d[j] = 1
            else:
                d[j] = d[j]+1
  
    val =  max (d.values())
    l = len (arr)
    
    if val <l:
        return 0
    
    if val  ==1:
        return 1
    
    
    count  =0 
    for i in d.values():
        if i ==val:
            count = count +1
    return count      
        
       
    
arr = ['vtrjvgbj', 'mkmjyaeav', 'sibzdmsk']

result = gemstones(arr)

print (result)
