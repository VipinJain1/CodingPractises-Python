# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:14:11 2021

@author: VIP
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        ln = len(nums)
        for i in nums:
            if i in d.keys():
                d[i] +=1
                if d[i] == ln/2:
                    return i
            else:
                d[i] =1
                
        