# -*- coding: utf-8 
"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP

https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

Search an element in a sorted and rotated array
Difficulty Level : Medium
Last Updated : 13 Jul, 2021
 
An element in a sorted array can be found in O(log n) time via binary search. 
But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. 
So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.
 

"""

import random as rd

cnt =0

def searchElem(nums, start, end, elem):
    
    global cnt
    if (elem == nums[start] or elem == nums[end]):
        return elem
    
    mid =  start + int (( end - start ) / 2)
    if elem == nums[mid]:
        return elem
    
    if elem >= nums[start] and elem <= nums[mid]:
        cnt = cnt +1
        end = mid
        start = start 
        return searchElem(nums, start, end, elem)
     
    else:
        cnt = cnt +1
        end = end
        start = mid+1
        return searchElem(nums, start, end, elem)


def findElemfromSortedOrRottatedArray(nums,elem):
    ln = len(nums) -1
    start = 0
    end  =ln
    elm = searchElem(nums, start,end,elem)
    return elm
    
# Start Program from here

nums = rd.sample(range(0,1000), 122)
nums = [3,2,1,4,5,6,7,8,9,10]
elem = 9

print ("Nums are ...", nums)
print (" Number found is " ,findElemfromSortedOrRottatedArray(nums,elem))

print ("Number of Iterations are " ,cnt)









