# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:14:19 2021

Remove Element
https://leetcode.com/problems/remove-element/

@author: VIP
"""



nums = [0,1,2,2,3,0,4,2]
nums = [2]
val = 3

ln = len(nums) -1
count  =0
newcnt = 0
finalcount = 0
while (newcnt <=ln):
     if nums[newcnt] != val:
         nums[count] = nums[newcnt]
         count = count +1
         newcnt = newcnt +1
         finalcount = count
     else:
         newcnt = newcnt +1
         
while count <=ln:
    nums[count] = '_'
    count = count +1

print (nums[0:finalcount])
print (finalcount)
     