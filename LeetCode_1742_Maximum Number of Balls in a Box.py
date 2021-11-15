# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:01:31 2021

@author: VIP
"""

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range (lowLimit,highLimit+1):
            n = int ()
            n = sum([int (m) for m in list(str(i))])
            if n in d.keys():
                d[n] +=1
            else:
                d[n] = 1
        return max(d.values())