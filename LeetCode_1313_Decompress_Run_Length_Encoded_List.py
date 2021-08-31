# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:01:51 2021

@author: VIP
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        result = []
        if len(nums) <=1:
            return nums
        
        i =0
        ln = len(nums)
        while (i <ln-1):          
            freq =  nums[i]
            val = nums[i+1]
            i = i+2
            result.extend([val]*freq)
        return result 
            
            
        