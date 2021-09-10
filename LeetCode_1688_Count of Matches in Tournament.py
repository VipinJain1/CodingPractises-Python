# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:57:38 2021

@author: VIP
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n ==0:
            return 0
        cnt = 0
        while (n >1):
            cnt = cnt + int (n/2)
            n = n - int (n/2)
        return cnt
    
        