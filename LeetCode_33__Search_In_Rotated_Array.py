# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:15:37 2021

https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

@author: VIP
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        else:
            return -1
            
        