# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:01:30 2021

@author: VIP
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        from itertools import permutations
        
        l = permutations(nums)
        d = dict()
        for i in  l:
            d[i] =i
        
        return d.keys()
            
        