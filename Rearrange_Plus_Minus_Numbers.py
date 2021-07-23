# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP

Question From: https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/

Rearrange positive and negative numbers with constant extra space
Difficulty Level : Medium
Last Updated : 14 Jun, 2021
Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional data structure like hash table, arrays, etc. The order of appearance should be maintained.

Examples:  

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
A simple solution is to use another array. We copy all elements of original array to new array. We then traverse the new array and copy all negative and positive elements back in original array one by one. This approach is discussed here. The problem with this approach is that it uses auxiliary array and we’re not allowed to use any data structure to solve this problem.
One approach that does not use any data structure is to use use partition process of QuickSort. The idea is to consider 0 as pivot and divide the array around it. The problem with this approach is that it changes relative order of elements. The similar partition process is discussed here .
Let’s now discuss few methods which do not use any other data structure and also preserves relative order of elements.
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









