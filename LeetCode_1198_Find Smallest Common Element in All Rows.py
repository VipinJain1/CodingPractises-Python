# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:53:35 2021

@author: VIP
"""

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        import sys
        d = {}
        ln = len(mat)
        print (ln)
        for idx, data in enumerate (mat):
            for  val in data:
                if val in d.keys():
                    d[val].append(idx)
                else:
                    d[val] = [idx]
        mn = sys.maxsize
        print ("Dict", d)
        found = False
        for item, val in d.items():
            if len(val) ==ln:
                if mn > item:
                    found = True
                    mn = item
        if found is False:
            return -1
            
        return mn            