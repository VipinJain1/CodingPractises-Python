# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:30:07 2021

@author: VIP
"""


arr =[1,2,2,3]
arr =[3,2,3,23,3,3,3]
#arr = [1,2,3,1,2,3,3]

def equalizeArray(arr):
    # Write your code here
    
    data = {}
    
    for i in arr:
        
        if i in data.keys():
            data[i] = data[i] +1
        else:
            data[i] =1
 
    valweNeed  = max(data.values())
    return len(arr) - valweNeed

print (equalizeArray(arr))