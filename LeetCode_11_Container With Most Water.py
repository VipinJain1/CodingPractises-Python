# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:39:11 2021

@author: VIP
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        end = len(height) -1
        start =0
        mx =0
        flipFlag = True
        while (start<end):
   
            mn =  min(height[start], height[end]) 
            curremx = (end -start)* mn
            if mx < curremx:
                mx = curremx
          
            if height[start] < height[end]:
                start +=1
            else:
                end -=1
                
        return mx    
            
            
        