# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:49:15 2021

@author: VIP
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sum1 =0
        sum2 =0
        ln = len(piles)
        if ln <=1:
            return False
       
        start =0
        end =ln-1
        other1 =0
        other2 =0
        while (start <end):
            sum1 = sum1 + piles[start]
            other1= other1 + piles[end]
            start +1
            end  -=1
        
        start =0
        end = ln -1
        while (start <end):
            other2 = other2 + piles[start]
            sum2 = sum2 + piles[end]
            start +1
            end  -=1
    
        if sum1 > other1 or sum2 > other2:
            return True
        else:
            return False
            
        
            