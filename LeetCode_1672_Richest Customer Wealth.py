# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:00:14 2021

@author: VIP
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx =0
        for i in accounts:
            sm= sum(i)
            if mx < sm:
                mx = sm
        return mx
    