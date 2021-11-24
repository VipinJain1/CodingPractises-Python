# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:39:11 2021

@author: VIP

NOT FULLY WORKING
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        end =  len(nums) -1
        nearestNum = nums[end]
        for idx, val in enumerate (nums):
            start = idx+1
            while (start < end):
                expectedSum  = val + nums[start] + nums[end]
                if  expectedSum < target:
                    dist  = target - expectedSum
                    if dist < nearestNum:
                        nearestNum = dist
                    start +=1
                elif expectedSum >target:
                    dist  = expectedSum -target
                    if dist < nearestNum:
                        nearestNum = dist
                    end -=1
                elif expectedSum == target:
                    nearestNum = target
                    return target
                    
                
        return abs (target -nearestNum)        
        
        