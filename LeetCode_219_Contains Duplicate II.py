# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:22:23 2021

@author: VIP
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        ln  = len(nums)
        if ln ==0:
            return False
        found = False
        d = dict()
        for idx,val in enumerate (nums):
            if val in d.keys():
                # check for multiple values
                for i in d[val]:
                    if abs (idx -i) <=k:
                        found = True
                        return True
               
                d[val] += [idx]
                   
            else:
                d[val] = [idx]
        
        return found
    
    
nums = [1,2,3,1,2,3]
k =2

obj = Solution()
status  = obj.containsNearbyDuplicate(nums,k)
print (status)