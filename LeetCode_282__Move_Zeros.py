# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:56:28 2021

https://leetcode.com/problems/move-zeroes/submissions/

@author: VIP
"""



def moveZeroes(nums):
    cnt =0
    for i in nums:
        if i ==0:
            cnt +=1
    newcnt =0
    for i in nums:
        if i !=0:
            nums[newcnt] = i
            newcnt +=1
    for i in  range (cnt):
        nums[newcnt] = 0
        newcnt +=1
    return nums
            

nums = [0,1,0,3,12]
print (moveZeroes(nums))
