# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:13:44 2021

@author: VIP
"""

class Solution:
 def topKFrequent(self, words: List[str], k: int) -> List[str]:
 d = dict()

 for i in words:
 if i in d.keys():
 d [i] +=1
 else:
 d[i] =1
 import heapq
 print (d)
 result = []
 res = heapq.nlargest(k, sorted (d.items()), key = lambda x:x[1])
 for i in res:
 result.append(i[0])
 return result


Sent with a Spark
