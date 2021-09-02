# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 00:14:48 2021

@author: VIP
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ln = len(nums)
        if ln <=1:
            return nums
        zero =0
        one =0
        two = 0
        for i in nums:
            if i ==0:
                zero +=1
            if i ==1:
                one +=1
                
            if i ==2:
                two +=1
        count =0           
        for i in range (0,zero):
            nums[count] =0
            count +=1
        
        for i in range (0,one):
            nums[count] =1
            count +=1
            
        for i in range (0,two):
            nums[count] =2
            count +=1
         
        return nums
            