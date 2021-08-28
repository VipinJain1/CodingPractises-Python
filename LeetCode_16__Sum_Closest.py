# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:26:33 2021

@author: VIP
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
            
        
nums = [-1,2,1,-4]
target = 1    
        
print (threeSumClosest (nums, target))
