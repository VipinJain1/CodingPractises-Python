# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:33:33 2021

@author: VIP
"""

import math
class Solution:
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        end = max(nums)
        start =1
        ln = len(nums)
        if ln == threshold:
            return end
        
        res  = []
        while (start <=end):
            mid = (start+end)//2
            sm  =0
            for i in nums:
                sm = sm + math.ceil(i/mid)
            if sm > threshold:
                start = mid+1
            else:
                res.append(mid)
                end = mid
                #print (end)
               
            if (start ==end):
                break
        #print (res)
        return min (res)
    

nums  = [21212,10101,12121]
th = 1000000
obj = Solution()
ret = obj.smallestDivisor(nums,th)
print (ret)