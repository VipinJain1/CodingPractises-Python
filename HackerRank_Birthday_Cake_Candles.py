# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:48:18 2021

@author: VIP
"""

def birthdayCakeCandles(candles):
    # Write your code here
    
    mx = max(candles)
    count =0
    for i in candles:
        if i == mx:
            count = count +1
    return count         


candles = [3,2,1,3]
print (birthdayCakeCandles(candles))