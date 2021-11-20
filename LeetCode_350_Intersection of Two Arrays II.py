# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:39:15 2021

@author: VIP
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2  = {}
        res  =[]
        for i in nums1:
            if i in d1.keys():
                d1[i] +=1
            else:
                d1[i] =1
        print ("D1",d1)
        
        for i in nums2:
            if i in d2.keys():
                d2[i] +=1
            else:
                d2[i] =1
        
        print ("D2", d2)
        res  = []
        for i in d2.keys():
            if i in d1.keys():
                res.extend([i]*min(d1[i],d2[i]))
        return res        
            