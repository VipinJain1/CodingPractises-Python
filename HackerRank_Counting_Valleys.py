# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:28:43 2021

@author: VIP
"""

def countingValleys(steps, path):
    # Write your code here
    
    count =0
    sum = 0
    for i in path:
        
        if i == 'D':
            sum = sum -1
        else:
            sum  = sum+1
       
            if sum ==0:
                count  = count +1
        
    return count 



path = ['U','D','D','D','U','D','U','U']
steps = 9
print (countingValleys(steps, path))