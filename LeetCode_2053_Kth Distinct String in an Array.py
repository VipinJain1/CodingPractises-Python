# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 08:10:50 2021

@author: VIP
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ln =len(arr)
        d ={}
        for i in arr:
            if i in d.keys():
                d[i] +=1
            else:
                d [i] =1
        cnt =0        
        print (d)
        for i in arr:
            if d[i] ==1:
                cnt +=1
            if cnt ==k and d[i] ==1:
                return i
        if cnt <k:
            return ""
                