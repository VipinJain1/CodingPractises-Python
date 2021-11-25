# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:11:24 2021

@author: VIP
"""

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt =0
        ln = len(nums)
        for i in range(0,ln):
            for j in range (0, ln):
                if nums[i]+nums[j] == target and i!=j:
                    cnt +=1
        return cnt
                    
        