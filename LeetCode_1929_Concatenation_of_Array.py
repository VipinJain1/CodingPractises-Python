# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:19:24 2021

https://leetcode.com/problems/concatenation-of-array/submissions/

@author: VIP
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans  = []
        ans.extend(nums)
        ans.extend (nums)
        return ans
        