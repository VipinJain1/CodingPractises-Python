# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:57:09 2021

@author: VIP
"""

class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        l1 = []
        l1 = s.split()
        print (l1)
        for c in l1:
            ans += 1
        return ans