# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:12:29 2021

@author: VIP
"""

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1  = sorted(nums1)
        nums2 = sorted(nums2)[::-1]
        
        ln = len(nums1)
        ln1 =len(nums2)
        if ln != ln1:
            return -1
        sm =0
        for i in range (0,ln):
            sm = sm + nums1[i] * nums2[i]
        return sm    
                       
        