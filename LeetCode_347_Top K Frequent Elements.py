# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:12:18 2021

@author: VIP
"""

class Solution:
 def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 ln = len(nums)
 if ln <k:
 return
 d = dict()
 for i in nums:
 if i in d.keys():
 d[i] +=1
 else:
 d[i] =1
 import heapq

 res = heapq.nlargest (k, d.items(), key = lambda x: x[1])
 result = []
 for i in res:
 result.append(i[0])

 return result

Sent with a Spark
