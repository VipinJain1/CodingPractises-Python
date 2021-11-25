# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:53:37 2021

@author: VIP
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ln = len(s)
        if ln ==0:
            return None
        st = list(s)
        i=0
        while (i <ln):
            if i+1 <ln:
                st[i:i+k] = st[i:i+k][::-1]
            i = i+2*k
        return "".join(st)    
            
            
            
            
            