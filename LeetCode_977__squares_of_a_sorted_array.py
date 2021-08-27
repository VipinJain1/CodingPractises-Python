# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:39:05 2021
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

@author: VIP
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        A = []
        A= [i*i for i in nums]
        return sorted (A)
        