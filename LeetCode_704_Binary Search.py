# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:39:12 2021

@author: VIP
"""

class Solution:
    def binSearch(self,nums, start, end, target):
        ret = -1
        while (start <=end):
            mid = (start + end)//2
            if  target > nums[mid]:
                start = mid+1
            elif target < nums[mid]:
                end = mid-1
            elif target == nums[mid]:
                return mid
            else:
                return 
            
        return ret
            
       
    def search(self, nums: List[int], target: int) -> int:
        start =0
        end = len(nums) -1
        if end == -1: 
            return -1
        return self.binSearch(nums,start,end,target)
        
        