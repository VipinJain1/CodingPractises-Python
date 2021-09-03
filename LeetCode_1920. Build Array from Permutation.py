# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:22:07 2021

@author: VIP
"""

class Solution:
    
    def buildArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln <=1:
            return nums
        res = []
        for i in range (0,ln):
            res.append( nums[nums[i]])
        return res
        
        

