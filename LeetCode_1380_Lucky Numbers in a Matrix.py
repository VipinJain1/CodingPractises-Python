# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:59:23 2022

@author: VipLeo
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        mn = {min(row) for row in matrix}
        mx = {max(column) for column in zip(*matrix)}
        type(mn)
        return mn & mx
    
    
            
       
            