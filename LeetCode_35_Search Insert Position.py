# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:47:58 2021

@author: VIP
"""

class Solution():
    
    def searchInsert(self, nums, target) -> int:
        
        def getIndex(nums,target,start,end) -> int:
            mid = (start+end)//2
            
            if target > nums[mid -1]:
                return mid
            if mid <end:
                if target < nums[mid]:
                    return mid
             
            if target > nums[mid]:
                getIndex (nums, target,mid, end)
                
            else:
                getIndex (nums, target,start, mid)
                
        
        #### Start Program ######
        
        if target == None:
            return
        ln = len(nums)
        
        start = 0
        end = ln
        
        if ln == 0:
            return None
        
        if ln ==1:
            if target >nums[0]:
                return 1
            else:
                return 0
            
        try:
            idx = nums.index(target)
            if idx != None:
                return idx
        except:
            idx = getIndex(nums,target,start,end)
            return idx
    
    
nums = [1,2]
target = 0
idx = Solution()
print (idx.searchInsert(nums,target))