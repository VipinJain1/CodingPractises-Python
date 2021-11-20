# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 08:57:44 2021

@author: VIP
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        ln =len(nums)
        if ln <=2:
            return sum (nums)
        nums.sort()
        
        start =0
        end = ln
        res =[]
        while (start < end):
            res.append(nums[start] + nums[end-1])
            start +=1
            end -=1
        return max(res)
            
            
            