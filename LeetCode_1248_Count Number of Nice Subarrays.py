# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:25:07 2021

@author: VIP
"""

class Solution:
    def numberOfSubarrays(self, nums, k):
        
        ln = len(nums)
        
        if ln <k:
            return 0
        cnt =0
        total =0
        idx = 0
        
        for idxx,i in enumerate (nums):
            if i %2 !=0:
                cnt +=1
            if cnt == k:
                total +=1
                idx = idxx
                break
        for i in range (1,ln-idx+1):
            if nums[i-1] %2 ==1 and nums[i+idx-1] %2==1:
                total +=1
            elif nums[i-1] %2 != 1 and nums[i+idx-1] %2 !=1:
                 total +=1
                  
        return total   
            
nums =[1,1,2,1,1]
k=3
obj = Solution()
res = obj.numberOfSubarrays(nums,k)
print (res)