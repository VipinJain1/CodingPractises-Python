# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:46:39 2021

@author: VIP
"""

class Solution:
    def search(self,nums, start, end, target, leftBias):
        i =-1
        while (start <= end):
            mid = (start+end)//2
            if target > nums[mid]:
                start = mid+1
            elif target < nums[mid] :
                end = mid-1
            else:
                i = mid
                if leftBias:
                    end = mid -1
                else:
                    start = mid +1
        return i
      
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        if ln ==0:
            return [-1,-1]
        start = 0
        end  = ln -1
        left  = self.search(nums,start,end,target, True)
        right = self.search(nums,start,end,target, False)
        
        return [left, right]
        
        