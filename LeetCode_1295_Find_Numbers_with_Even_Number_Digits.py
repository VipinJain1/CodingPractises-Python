# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:09:46 2021

@author: VIP
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ln  = len(nums)
        if ln ==0:
            return None
        count  =0
      
        for i in nums:
            if (len(str(i))) %2 == 0:
                count += 1
        return count      
  
                
            
        
        