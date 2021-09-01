# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:57:49 2021

@author: VIP
"""

def maxProfit(prices):
    mxP = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            mxP, prices[i] = max(mxP, prices[i] - prices[i-1]), prices[i-1]
    return mxP
   
prices = [7,1,5,3,6,4]

print (maxProfit(prices))