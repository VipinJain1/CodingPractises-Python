# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:35:30 2021

@author: VIP
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        ln  = len(nums)
        res  = []
        
        if ln >=1:
            res.append(nums[0])
        if ln >=2:
            res.append(max (nums[0], nums[1]))
            
        for i in range (2,ln):
            res.append(max((nums[i] + res[i-2]), res[i-1]))
        return res[ln-1]
        
        
        
            