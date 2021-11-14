# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:47:04 2021

@author: VIP
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans = [None] * 2*ln
        for i in range (0,ln):
            ans[i] = nums[i]
            ans[i+ln] = nums[i]
        return ans