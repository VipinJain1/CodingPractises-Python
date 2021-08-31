# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:10:10 2021

@author: VIP
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        ln  = len (s)
        if ln <=1:
            return s
        result = []
        v = s.split(' ')
        for i in v:
            result.append (i[::-1])
        
        s = ' '.join (result)
        return (s)
        
        