# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:26:20 2021

@author: VIP
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        start =0
        nums.sort()
        res  = []
        while (start <ln):
            res.append(nums[start])
            start +=1
            if start<ln:
                res.append(nums[ln-1])
                ln -=1
         
        return res
    
        
      
            
            
            
            
        
        
            
n = [1,2,3,4,5,6,7,8,9,0,162,234,33,78,567,12,98,712,384,65]
obj = Solution()
print (obj.rearrangeArray(n))
