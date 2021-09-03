# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:11:21 2021

@author: VIP
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        
        s = s.strip()
        ln = len(s)
        if ln ==0:
            return None
        
        s =  ' '.join((s.split(' ')[::-1]))
        return re.sub(r"\s+", " ", s)
        
        