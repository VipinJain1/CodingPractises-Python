# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:03:05 2021

@author: VIP
"""

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        if ln ==0:
            return None
        cnt= 0
        for i in range (0, ln):
            for j in range (i+1, ln):
                
                if i<j and (abs(nums[i] - nums[j]) ==k):
                    cnt +=1
        return cnt
                    
                
        