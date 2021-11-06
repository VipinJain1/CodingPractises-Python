# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:54:24 2021

@author: VIP
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        d = {}
        for i in arr:
            d[i] =1
        cnt =0
        for i in range (1,300000):
            if i not in d.keys():
                cnt +=1
                if cnt ==k:
                    return i
                
            
            
            
            
arr = [2,3,4,7,11]
k = 5 
obj = Solution()
missing = obj.findKthPositive(arr,k)
print (missing)