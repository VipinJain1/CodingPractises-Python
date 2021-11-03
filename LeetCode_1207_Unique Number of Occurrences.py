# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:37:00 2021

@author: VIP
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d ={}
        flag = True
        for  i in arr:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] = 1
        d1 = {}
        print (d)
        for key, val in d.items():
            if val in d1.keys():
                flag = False
                return flag
            else:
                d1[val] = 1
        return flag
            