# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:28:07 2021

@author: VIP
"""

"""
def threeSum (nums):
        ln = len(nums)
        
        if ln <3:
            return []
        
        res = []
        for i in range (0, ln):
            for j in range (i+1, ln):
                for k in range (j+1, ln):
                    
                    if (nums[i] + nums[j] + nums[k] ==0) and (i !=j and j!=k and i != k):
                        
                        if sorted([nums[i],nums[j],nums[k]]) not in res:
                            data = sorted ([nums[i],nums[j],nums[k]])
                            res.append (data)
                    
        return res

"""

    
    
    
nums = [-1,0,1,2,-1,-4]
print (threeSum (nums))