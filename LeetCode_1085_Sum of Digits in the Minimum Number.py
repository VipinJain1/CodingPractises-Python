# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 08:08:18 2021

@author: VIP
"""

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        x = min(nums)
        print (x)
        sm =0
        for i in (str(x)):
            sm = sm + int (i)
            x=sm
                 
        if x%2==0:
            return 1
        else:
            return 0
            
        