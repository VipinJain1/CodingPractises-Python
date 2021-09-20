# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:02:51 2021

@author: VIP
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        from itertools import permutations
        
        return permutations(nums)
    
            
        