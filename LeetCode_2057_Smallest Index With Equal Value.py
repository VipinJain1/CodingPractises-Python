# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:36:48 2021

@author: VIP
"""

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        for idx, num in enumerate (nums):
            if idx %10 == num:
                return idx
        
        return -1
    