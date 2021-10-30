# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:29:37 2021

@author: VIP
"""

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 ={}
        d2 ={}
        
        for idx, i in enumerate (nums1):
            if i in d1.keys():
                d1[i] += [idx]
            else:
                d1[i] = [idx]
        

        for idx, i in enumerate (nums2):
            if i in d2.keys():
                d2[i] += [idx]
            else:
                d2[i] = [idx]
        res =[]
        print (d2)
        for  i in nums1:
            res.append(d2[i][0])
        return res
            