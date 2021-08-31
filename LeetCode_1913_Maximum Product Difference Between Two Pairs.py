# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:03:48 2021

@author: VIP
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        res =  sorted(nums)
        ln = len (nums)
        return res[ln-1]* res[ln-2] - res[0] *res[1]
         