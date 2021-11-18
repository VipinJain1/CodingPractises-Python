# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 22:32:19 2021

@author: VIP
"""

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        sm =0
        cnt =0
        for i in range (0, len(weight)):
            
            sm = sm + weight[i]
            cnt +=1
            if sm > 5000:
                return cnt -1
                
        return cnt 
            
        
        