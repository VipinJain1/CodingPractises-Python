# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:28:41 2021

@author: VIP
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        d1 = dict()
        d2 = dict()
        
        for i in edges:
            if i[0] in d1.keys():
                d1[i[0]] +=1
            else:
                d1[i[0]] =1
                
            if i[1] in d2.keys():
                d2[i[1]] +=1
            else:
                d2[i[1]] =1
        v1  = max (d1.values())
        v2  = max (d2.values())
        if v1> v2:
            return [key for key, val in d1.items() if val == v1][0]
        else:
            return [key for key, val in d2.items() if val == v2][0]
        
