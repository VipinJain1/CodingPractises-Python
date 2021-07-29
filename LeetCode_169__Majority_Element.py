# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:46:30 2021

169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

https://leetcode.com/problems/majority-element/
 

@author: VIP
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        
        for i in range (len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] = d[nums[i]] +1
            else:
                d[nums[i]] =1

        for key, i in d.items():
            if i >= len(nums)/2:
                return (key )
            
            