# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:34:04 2021

@author: VIP
"""


def firstMissingPositive(nums):
    import heapq as heap
    heap.heapify(nums)
    i =1
    while (nums):
        if i != heap.heappop(nums):
            return i
        else:
            i=+1
            
    

nums = [1,7,8,9,11,12]

print (firstMissingPositive(nums))
    