# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:12:46 2021


https://leetcode.com/problems/number-of-1-bits/
@author: VIP
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt =0 
        while (n):
            cnt += n&1
            n >>= 1

        return cnt