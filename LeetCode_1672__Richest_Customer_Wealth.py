# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:36:21 2021

https://leetcode.com/problems/richest-customer-wealth/submissions/

@author: VIP
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if len(accounts) ==0:
            return None
        
        mx = 0
        for i in accounts:
            
            if mx < sum(i):
                mx = sum(i)
        
        return mx
        
        
        