# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:26:45 2021

@author: VIP
"""

def numberOfSteps(num):
    if num ==0:
        return 0
        
    count =0
    
    while (num !=0):
        
        if num%2 ==0:
            num = num/2
        else:
            num = num-1
        count = count +1
    return count



num = 14

print (numberOfSteps(num))