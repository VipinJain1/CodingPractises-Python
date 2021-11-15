# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:59:29 2021

@author: VIP
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        res  = []
        for num in range (0,n+1):
            res.append(sum([int (i) for i in bin(num)[2:]]))
        return res
            
        