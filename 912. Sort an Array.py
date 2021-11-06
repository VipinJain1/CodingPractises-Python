# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:53:47 2021

@author: VIP
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq
        heapq.heapify(nums)
        ln = len(nums)
        return heapq.nsmallest(ln,nums)
        