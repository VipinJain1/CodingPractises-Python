# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:13:37 2021

@author: VIP
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n ==0:
            return False
        if n==1:
            return 1
        
        cnt =1
        x = int (sqrt(2*n)) 
        
        if (x * (x+1))/2 > n:
            return x-1
        else:
            return x
    