# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:28:18 2021

https://leetcode.com/problems/power-of-two/

@author: VIP
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if  n== 1:
            return True
        if n ==0:
            return False
        if (n & (n -1)) ==0:
            return True
        else:
            return False