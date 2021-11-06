# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 09:54:05 2021

@author: VIP
"""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        ln = len(arr)
        
        if ln <k:
            return 0
        dk ={}
        
        threshold = threshold *k
        resCnt =0
        sm = sum(arr[0:k])
        if sm >=threshold:
            resCnt +=1
        
        for i in range (1, ln-k+1):
            sm = sm - arr[i-1] + arr[i+k-1]
            if sm >= threshold:
                resCnt +=1
                    
        return resCnt
    
            

arr= [7,7,7,7,7,7,7]
k =3
t =5
obj = Solution()
res= obj.numOfSubarrays(arr,k,t)
print (res)       
