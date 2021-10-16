# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 09:35:16 2021

@author: VIP
"""

def kClosest(points, k):
    d = {}
    result = []
    for i in points:
        key = i[0]**2 + i[1]**2
        if key in d.keys():
            d[key] += [i]
        else:
            d[key ] = [i]
    
    
    items  = list (d.items())
    
    import heapq
    heapq.heapify(items)

    
    res = heapq.nsmallest(k,items)
    for i in res:
        for j in i[1]:
            result.append(j)
    return result[0:k]
            
        
k=2

points =  [[-5,4],[-6,-5],[4,6]]

print (kClosest(points,k))