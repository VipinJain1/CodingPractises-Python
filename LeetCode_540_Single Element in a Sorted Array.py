# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 08:58:33 2021

@author: VIP
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] =1
        for i in d.keys():
            if d[i] ==1:
                return i
        return None
    