# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:47:33 2021

@author: VIP
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return (nums[0]-1) * (nums[1]-1)
        