# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:47:48 2021

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

https://leetcode.com/problems/two-sum/


@author: VIP

"""

def twoSum(nums, target):
    
    dt = dict()
    
    for idx, dta in enumerate (nums):
        
        if dta in dt.keys():
            dt[dta].append(idx)
        else:
            dt[dta] = [idx]
    
    for data, idx in dt.items():
        
        if ((target - data) in dt.keys()):
            if len (dt[data]) >1:
                return (dt[data])
            elif (idx[0] != nums.index(target -data)):
                return (idx[0], nums.index(target -data))
                
V = [3,2,4]
V=[2,5,5,11]
#V=[3,3]
target =10
print (twoSum(V, target))
