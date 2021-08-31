# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:00:46 2021

@author: VIP
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ln = len(nums)
        
        if ln <=1 or k ==0:
            return None
        
        found = False
        for i in range (0,ln):
            for j in range (i+1, ln):
                if (nums[i] == nums[j] and abs (i-j) <=k):
                    found = True
        return found
    
                    
            
            