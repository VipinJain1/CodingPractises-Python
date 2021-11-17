# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:39:55 2021

@author: VIP
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        d1 = {}
        arr1.sort()
        res = []
        for i in arr1:
            if i  in d.keys():
                d[i] +=1
            else:
                d[i]=1
        
        for i in arr2:
            if i  in d1.keys():
                d1[i] +=1
            else:
                d1[i]=1
        for i in arr2:
            res.extend([i]*d[i])

        for i in arr1:
            if i  not in d1.keys():
                res.append(i)
        return res 
        
     
        