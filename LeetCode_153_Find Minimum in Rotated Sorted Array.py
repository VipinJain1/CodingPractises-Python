# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:26:20 2021

@author: VIP
"""
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ln = len(nums)
        res = []
        nums.sort()
        res.append(nums[0])
   
        for i in range(1,ln-1):
            nums[i], nums[ln-1] = nums[ln-1],nums[i]
            avg =  (nums[i-1] + nums[i+1])//2
            if avg == nums[i]:
                break
            else:
                res.append(nums[i])
        
        if len(res) ==1:
            return []
        else:
            res.append(nums[ln-1])
            return res
        
        
            
n = [1,2,3,4,5,6,7,8,9,0,162,234,33,78,567,12,98,712,384,65]
obj = Solution()
print (obj.rearrangeArray(n))
