# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:49:16 2021

@author: VIP
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d.keys():
                return i
            else:
                d[i] =1
                
            