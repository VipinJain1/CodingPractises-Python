# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:56:07 2021

@author: VIP
"""

def circularArrayRotation(a, k, queries):
   # Write your code here
    ln = len(a)
    result = []   
    
    if queries == None or a == None:
        return None
    
    if k >ln:
        k = k%ln
        
    for i in range(0,k):
        a= [a[ln-1]] + a[:-1]

    for i in queries:
        if i > ln -1:
            return None
        result.append(a[i])
    return result
      
        
a = [3,4,5]
k =200
queries = [1,2]

print (circularArrayRotation(a, k, queries))
    