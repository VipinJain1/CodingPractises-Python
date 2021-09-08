# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 00:49:41 2021

@author: VIP
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln <=1:
            return nums
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] =1
            else:
                d[i] = d[i] + 1
        
        cnt = int (ln/3)
        res  =[]
        for key, val in d.items():
            if val > cnt:
                res.append(key)
        return res
    
        
        
        