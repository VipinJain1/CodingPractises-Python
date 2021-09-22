# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:26:33 2021

@author: VIP
"""
"""
def threeSumClosest(nums, target):
        
        if len (nums) <3:
            return None
        dist =100000000
        prevSum = 1000000
        
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                 for k in range (j+1, len(nums)):
                        
                        if ( abs( target -  (nums[i] + nums[j] + nums[k])) <= dist and (i!=j and j!=k)):
                            dist = abs (nums[i] + nums[j] + nums[k])
                       
        return dist  
            
"""


# Still Failed
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ln = len (nums)
        if ln <3:
            return None
        
        nums = sorted(nums)
        cnt =0
        res = 0
        dist = 1000000 
        while (cnt <ln -2):
            
            if abs((abs (nums[cnt] + nums[cnt+1] + nums[cnt+2]) - target)) < dist:
                dist =  abs((abs (nums[cnt] + nums[cnt+1] + nums[cnt+2]) - target))
                res = nums[cnt] + nums[cnt+1] + nums[cnt+2]
            cnt +=1
            
        return res
    
nums =[0,2,1,-3]
target = 1    
        
print (threeSumClosest (nums, target))
