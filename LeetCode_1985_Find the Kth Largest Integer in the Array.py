# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:32:18 2021

@author: VIP
"""

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        import heapq
        numsList =[]
        if k > len(nums):
            return None
        
        for i in nums:
            heapq.heappush(numsList, int(i))
        #print (numsList)
        
        #heapq.heapify(numsList)
        num = heapq.nlargest(k,numsList)
        return str (num[k-1])
        