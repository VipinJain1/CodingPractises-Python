# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:30:13 2021

@author: VIP
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        print (mx)
        idx = nums.index(mx)
       
        for i in nums:
            if mx < i*2 and i !=mx:
                return -1
        return idx
            