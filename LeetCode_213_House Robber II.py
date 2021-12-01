# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 08:47:38 2021

@author: VIP
"""

class Solution:
    def houseRob(self,nums):
        res  = []
        ln = len(nums)
        if ln >=1:
            res.append(nums[0])
        if ln >=2:
            res.append(max (nums[0], nums[1]))
            
        for i in range (2,ln):
            res.append(max((nums[i] + res[i-2]), res[i-1]))
        return res[ln-1]
        
        
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln ==0:
            return 0
        if ln ==1:
            return nums[0]
        if ln ==2:
            return max(nums[0],nums[1])
        
        choice1 = self.houseRob(nums[0:ln-1])
        choice2 = self.houseRob(nums[1:])
        return max( choice1, choice2)
    