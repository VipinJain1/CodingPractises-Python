# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:42:57 2021

@author: VIP
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ln = len(s)
        lnpart = len(part)
        while (s):
            try:
                loc = s.index(part)
                s = s[0:loc] + s[lnpart+loc:ln]
            except:
                return s
        return ""    