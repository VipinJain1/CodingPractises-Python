# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:20:06 2021

@author: VIP
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n ==1:
            return [0]
        cnt = int (n/2)
        while (cnt):
            result.append (cnt)
            result.append (-cnt)
            cnt = cnt-1
        if n%2 ==0:
            return result
        else:
            result.append (0)
            return result 
        
            
            
            