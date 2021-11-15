# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:00:54 2021

@author: VIP
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        result = []
        for idx,val in enumerate (groupSizes):
            if val in d.keys():
                d[val].append(idx)
            else:
                d[val] = [idx]
        for k, val in d.items():
            if len(val) >k:
                    n = len(val)//k
                    for i in range (0,n*k,k):
                        result.append(val[i:k+i])
            else:
                result.append(val)
        return result
                
        