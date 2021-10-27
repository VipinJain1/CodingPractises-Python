# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:02:45 2021

@author: VIP
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums) -1
        
        if ln ==0:
            return False
        
        r = 0
        g = 0
        b = 0
        for i in nums:
            if i ==0:
                r +=1
            if i ==1:
                g +=1
            if i ==2:
                b +=1
        for i in  range (0,r):
            nums[i]= 0
        for i in  range (0,g):
            nums[i+r]= 1
        for i in  range (0,b):
            nums[i+r+g]= 2