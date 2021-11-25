# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:09:47 2021

@author: VIP
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln <= 1:
            return 0
        if ln ==2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        if nums[ln-1] > nums[ln-2]:
            return ln-1
        for i in range (1,ln-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return 0
        