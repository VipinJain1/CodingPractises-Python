# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 14:54:40 2021


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/search-insert-position/
 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

@author: VIP

"""

nums = [1,3,5,6]
target = 2

s = 0
e = len (nums) -1

while (s<e):
    
    mid  =  (e - s)//2
    
    if (target  == nums[mid]):
        print ( mid)
    
    if target > nums[mid]:
        s = mid+1
    else:
        e = mid
        
print (s)                      


"""
counter = 0

def findNum(nums,target,index):
    global counter 
    ln = len (nums)
    
    if ln == 1:
        return index
    
    mid = int (ln /2)
    
    counter = counter +1
    if nums[mid] == target:
        
        index = index + mid
        return index
    else:
        return index
    
    if target >= nums[mid]:
        nums = nums[mid:ln]
        index = index + mid
        start = mid
        return findNum(nums,target,index)
    else:
        nums = nums[0:mid]
        index = index
        return findNum(nums,target,index)

nums = [1,3,5,6]
target = 2
index =0
print (findNum(nums,target,index))

print ("Counter  === ", counter)
"""