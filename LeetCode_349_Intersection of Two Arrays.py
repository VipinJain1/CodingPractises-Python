# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:12:49 2021

@author: VIP
"""

class Solution:
 def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
 nm1 = set(nums1)
 nm2 = set(nums2)

 result = []
 d = dict()
 for i in nm1:
 d[i] =i
 for i in nm2:
 if i in d.keys():
 result.append(i)
 return result

Sent with a Spark
