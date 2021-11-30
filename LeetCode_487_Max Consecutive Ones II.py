# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:15:40 2021

@author: VIP
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start =0
        k =1
        end  = len(nums)
        newstart =0
        mx =1
        while (start <end):
            if nums[start] ==0:
                k -=1
            if k ==0:
                mx  = max(mx, (start - newstart +1))    
               
            if k <0:
                while (nums[newstart] !=0):
                    newstart +=1
                if nums[newstart] ==0:
                    newstart +=1
                    k +=1
            start +=1
        if mx ==1:
            return start -newstart
        return  mx
            
                
                
        
                
                
nums = [1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1]
obj = Solution()
res = obj.findMaxConsecutiveOnes(nums)
print (res)