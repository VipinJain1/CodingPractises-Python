# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:56:19 2021

@author: VIP
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end  = len(nums)
        result  =[]
        while (start <end-1):
            result.append(min (nums[start], nums[start+1]))
            start = start+2
        return sum (result)
            
            
            
            
            
            
            
    