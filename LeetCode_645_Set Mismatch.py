# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:13:24 2021

@author: VIP
"""

class Solution:
 def findErrorNums(self, nums: List[int]) -> List[int]:
 ln =len(nums)
 d = dict()
 duplicate = None
 res = []
 for i in nums:
 if i in d.keys():
 duplicate =i
 res.append(duplicate)
 d[i] += 1
 else:
 d[i] =1
 for i in range (1,ln+1):
 if i not in d.keys():
 res.append(i)
 return res

Sent with a Spark
