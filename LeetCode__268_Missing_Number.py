# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:49:50 2021

@author: VIP
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ln  = len(nums) +1
        sm = int ((ln *(ln-1))/2)
        sm1 =sum(nums)
        return int (sm -sm1)
    