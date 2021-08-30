# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:06:59 2021

@author: VIP
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ln = int(len(nums)/2)
        if n > ln or ln <=1:
            return nums
        cnt = n
        a = [] 
        for i in range (0, ln):
            a.append(nums[i])
            a.append (nums[n+i])
        
        return a
    
            
        