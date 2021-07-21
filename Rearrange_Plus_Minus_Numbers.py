# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP
"""

import random as rd


def reArrange_Plus_Minus_Numbers_Sort(nums):
    return sorted (nums)
        

def numSwap(nums,start,end):
      
      if (nums[end] > 0):
          while (nums[end] > 0):
              end = end -1
      nums[start], nums[end]  = nums[end], nums[start]
      end = end -1
      return end

        
def reArrange_Plus_Minus_Numbers(nums):
    ln = len(nums) -1
    start  =0
    
    while  (start <=ln):
        if nums [start] >=0:
            ln = numSwap(nums, start, ln)
            start = start +1
        else:
            start = start +1
            
    return nums
            
         
print (" Add number of elements")
n =int (input())
nums =rd.sample(range(-30, 30), n)
print (nums)

print (" Numbers are arranged by minus and plus " , reArrange_Plus_Minus_Numbers_Sort(nums))


print (" Numbers are arranged by minus and plus " ,reArrange_Plus_Minus_Numbers(nums))









