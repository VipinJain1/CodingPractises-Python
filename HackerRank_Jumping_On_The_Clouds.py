# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:55:38 2021

@author: VIP
"""


def jumpingOnClouds(c):
    # Write your code here
    count =0
    i =0
    while (i <len(c)-1):
        if (c[i] ==0 or c[i+1] ==0) and c[i+2] ==1:
            count = count+1
            i = i+1
        elif  (c[i] ==0 or c[i+1] ==0) and c[i+2] ==0:
            count = count+1
            i = i+2
            
        elif (c[i] ==0  or c[i+1] ==1 ) or (c[i] ==1  or c[i+1] ==0 ):
            count = count+1
            i = i+1
        
    return count     



c = [0, 0, 1, 0, 0, 1, 0]
print (jumpingOnClouds(c))