# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 08:09:49 2021

@author: VIP
"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d ={}
        for i in s:
            if i in d.keys():
                d[i] +=1
            else:
                d[i]=1
                
        ln = len(d)
        chk = d[s[0]]
        for i in d.values():
            if i != chk:
                return False
            
        return True  