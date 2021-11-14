# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:44:56 2021

@author: VIP
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        result  =[]
        ln = len(arr)
        d = {}
        for i in arr:
            binval = (list(bin(i)[2:])).count ('1')
            if binval in d.keys():
                d[binval].append(i) 
            else:
                d[binval] = [i]
            
        import heapq
        res = heapq.nsmallest(ln,d.items(),key= lambda x: x[0])
        for i in res:
            print (i)
            result.extend(sorted (i[1]))
        return result 