# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:52:29 2021

@author: VIP
"""

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        d = {}
        mx = -1
        for i in nums:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] =1
        for key, val  in d.items():
            if val==1 and mx < key:
                mx = key
        return mx 
            
            