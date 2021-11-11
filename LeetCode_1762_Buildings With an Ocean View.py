# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:57:23 2021

@author: VIP
"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ln = len(heights)
        size = ln -1
        mx = heights[size]
        result = []
        result.append(size)
        ctr = size-1
        while (ctr >=0):
            if mx < heights[ctr]:
                result.append(ctr)
                mx = heights[ctr]
            ctr -=1
        return sorted(result) 
    
            
            
            

        
            
            

        