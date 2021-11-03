# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:35:41 2021

@author: VIP
"""

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d ={}
        for i in items:
            key = i[0]
            val = i[1]
            if key in d.keys():
                d[key] += [val]
            else:
                d[key] = [i[1]]
        res = []         
        for key, val in d.items():
            if len(val) >=5:
                sval = sorted(val)[::-1]
                print (sval)
                avg = int((sum(sval[0:5]))/5)
                res.append([key,avg])
        return sorted (res)        