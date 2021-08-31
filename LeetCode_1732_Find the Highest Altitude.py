# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:05:46 2021

@author: VIP
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        ln  = len(gain)
        if ln ==0:
            return 0
        result = []
        result.append(gain [0])
        count =0
        for i in range (1, ln):
            result.append( result [count] + gain [i])
            count = count +1
            
        if max (result) >0:
            return max (result)
        else:
            return  0
            
        