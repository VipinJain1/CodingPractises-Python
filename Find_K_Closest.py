# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 08:09:32 2021

@author: VIP
"""

class Solution:
 def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

     ln = len(arr)
     if ln <1:
     return 0
     if k > ln:
     return 0 
     d = {}
     for i in arr:
     val = abs (x-i)
     if val in d.keys():
     d[val] += [i]
     else:
     d[val] = [i]
    
     valList = list (d.items())
    
     import heapq
    
     print (d)
    
     heapq.heapify (valList)
     res = heapq.nsmallest(k,valList, key = lambda x:x[0])
     result =[]
     for i in res:
     result.extend(i[1])
     if len (result) >= k:
     return sorted(result[:k])


