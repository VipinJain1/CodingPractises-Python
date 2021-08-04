# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:04:42 2021

@author: VIP
"""

def icecreamParlor(m, arr):
    count =0
    for i in arr:
        if (m-i) in arr[count+1:]:
            idx1 =  count+1
            idx2= arr[count+1:].index(m-i)+count+1+1
            return [idx1,idx2]
        else:
            count = count +1
            
    
m = 4
arr = [2,2,4,3]
#m =4
#arr = [1,4,5,3,2]
print (icecreamParlor(m, arr))