# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:34:25 2021

@author: VIP
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        ln = len (s)
        if ln ==0:
            return None
        
        s = s.replace('a','')
        s = s.replace('i','')
        s = s.replace('e','')
        s = s.replace('o','')
        s = s.replace('u','')
        
        return s