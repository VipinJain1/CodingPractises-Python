# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:27:05 2021

@author: VIP
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        b =0
        cnt = 0
        num = 0
        for i in range (0,32):
            bit = n & 1
            n = n>>1
            num = (num <<1) ^ bit
        return num