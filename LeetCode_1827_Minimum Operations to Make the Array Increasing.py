# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:58:37 2021

@author: VIP
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ln = len(nums)
        if ln ==0:
            return
        mx =0
        for i in range (1,ln):
            if nums[i] <=nums[i-1]:
                val = (nums[i-1] - nums[i] ) +1
                nums[i] = nums[i] + val
                mx = mx+val
        return mx
                
            
            
            