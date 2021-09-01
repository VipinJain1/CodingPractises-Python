# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:07:34 2021

@author: VIP
"""

class Solution:
    def replaceDigits(self, s: str) -> str:
        
        ln = len(s)
        if ln <=1:
            return s
        cnt = 0
        s1 = str()
    
        while (cnt <ln):
            c1  = s[cnt]
            cnt = cnt+1
            if cnt <ln:
                c2  =   chr (ord (c1) +  int (s[cnt]))
                s1  = s1 + c1 +c2
            else:
                s1 = s1+c1
            cnt = cnt+1
        return s1
        