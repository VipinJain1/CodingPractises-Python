# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:27:49 2021

@author: VIP
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ln = len(nums)
        count =0
        for i in range (0,ln):
            for j in range (i+1, ln):
                if nums[i] == nums[j] and i !=j:
                    count = count +1
        return count
    
        
        
        
        
            