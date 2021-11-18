# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:00:58 2021

@author: VIP
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res1 =[]
        res2 =[]
        for i in nums:
            if i %2 ==0:
                res1.append(i)
            else:
                res2.append(i)
        
        res1.extend(res2)
        return res1