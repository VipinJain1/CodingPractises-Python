# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:37:00 2021

@author: VIP
"""

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        count  =0
        for i in patterns:
            if i in word:
                count +=1
        return count 
            
        