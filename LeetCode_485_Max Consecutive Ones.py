# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:30:01 2021

@author: VIP
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ln  = len(nums)
        
        if ln ==0:
            return  0
    
        if 1 not in nums:
            return  0

        cnt =1
        mxcnt = 0
        for i in  range (1, len(nums)):
            if nums[i-1] == nums[i] and nums[i] ==1:
                cnt +=1
            else:
                if mxcnt <cnt:
                    mxcnt =cnt
                cnt =1
        if mxcnt <cnt:
            mxcnt = cnt
        return mxcnt

            
    
            