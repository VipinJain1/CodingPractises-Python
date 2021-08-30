# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:28:45 2021

@author: VIP
"""

def runningSum(self, nums: List[int]) -> List[int]:
       ln = len(nums)
       nm = []
       nm.append(nums[0])
       if ln <=1:
           return nums
       for i in range (1,ln):
           nm.append (sum(nums[0:i+1]))
       return nm
    
nums = [1,2,3,4]

print (runningSum(nums))
