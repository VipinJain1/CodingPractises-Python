# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 07:58:15 2021

@author: VIP
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        d = dict()
    
        for i in set(nums1):
            d[i] = 1
        
        
        for i in set(nums2):
            if i in d.keys():
                d[i] +=1  
            else:
                d[i] = 1
       
         
        for i in set(nums3):
            if i in d.keys():
                d[i] +=1  
            else:
                d[i] = 1
        res = []
        for i in d.items():
            if i[1] >=2:
                res.append(i[0])
        return res
    
                