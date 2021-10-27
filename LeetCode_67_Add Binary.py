# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:09:36 2021

@author: VIP
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c =int()
        c= int (a,2) + int (b,2)
        return bin(c)[2:]
      