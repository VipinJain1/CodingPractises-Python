# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:39:18 2021

@author: VIP
"""



## Bubble Sort
arr = [2,4,12,2,3,5,67,87,843,2,3,45,76,8,89]

ln = len(arr)
for i in range (0,ln):
    for j in range (0,ln):
        
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
print (arr)

##Insertion Sort



