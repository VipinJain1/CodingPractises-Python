# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:15:33 2021

@author: VIP
"""

class Solution:
 def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
 ln = len(nums)
 if ln ==0:
 return
 res = []
 d = dict()
 for i in nums:
 d[i] = True
 for i in range (1,ln+1):
 if i not in d.keys():
 res.append(i)

 return res 

