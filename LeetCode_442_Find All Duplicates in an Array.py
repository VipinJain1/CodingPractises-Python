# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:21:14 2021

@author: VIP
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ln = len(nums)
        if ln <=1:
            return None
        d = {}
        res = []
        for i in nums:
            if i in d.keys():
                res.append(i)
            else:
                d[i] =1
        
        return res
                
            
        