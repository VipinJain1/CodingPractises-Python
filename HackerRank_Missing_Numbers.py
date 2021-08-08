# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:10:34 2021

@author: VIP
"""

def missingNumbers(arr, brr):
    # Write your code here
    a = dict()
    b = dict()
    
    missing = []
    for i in arr:
        if i in  a.keys():
            a[i] = a[i] +1
        else: 
            a[i] = 1
   # print (a)
    
    for i in brr:
        if i in  b.keys():
            b[i] = b[i] +1
        else: 
            b[i] = 1
    #print (b) 
    
    for key,data in b.items():
        if key not in a.keys():
            missing.append(key) 
        else:
            if a[key] != b[key]:
                diff  =  a[key] - b[key]
                #print (a[key], b[key])
                for i in range (abs(diff)):
                    if key not in missing:
                        missing.append(key)
            if b[key] != a[key]:
                diff  =  b[key] - a[key]
                #print (a[key], b[key])
                for i in range (abs(diff)):
                    if key not in missing:
                        missing.append(key)
                        
    #print (missing)
    return sorted (missing) 

arr = [203, 204, 205 ,206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

arr= [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
brr = [4 ,11, 7, 3, 7 ,10, 13, 4, 8, 12 ,11, 10, 14, 12]

result = missingNumbers(arr, brr)
print (result)