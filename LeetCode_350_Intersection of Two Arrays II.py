# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:25:18 2021

@author: VIP
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        d2 = dict()
        res = []
        for i in nums1:
            if i in d1.keys():
                d1[i] +=1
            else:
                d1[i] = 1
                
        for i in nums2:
            if i in d2.keys():
                d2[i] +=1
            else:
                d2[i] = 1
                        
        for i in d1.keys():
            if i in d2.keys():
                cnt = min (d1[i], d2[i])
                for ii in range (cnt):
                    res.append(i)
                    
        return res
    
            
        