# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:54:18 2021

@author: VIP
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted (s) == sorted(t):
            return True
        else:
            return False
        