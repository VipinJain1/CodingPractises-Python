# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:31:22 2021

@author: VIP
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n ==0:
            return  0
        mult =1
        sm = 0
        for i in str(n):
            mult =  int (i)*mult
            sm = sm + int (i)
        return mult - sm
            
        