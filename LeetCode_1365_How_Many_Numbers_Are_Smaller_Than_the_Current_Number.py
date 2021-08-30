# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:29:14 2021

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

@author: VIP
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range  (0,len(nums)):
            count =0
            for j in range (0,len(nums)):
                if (nums[i] > nums[j] and i !=j):
                    count = count +1
            result.append(count)
        return result
    
                    
            