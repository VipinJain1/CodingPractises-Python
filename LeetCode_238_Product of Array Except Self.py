# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:31:46 2021

@author: VIP
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln  == 0:
            return None
        res = []
        zrocnt =0
        loc = []
        mult =1
        for i in range (0, ln):
            if nums[i] ==0:
                    loc.append(i)
                    zrocnt +=1
                    if zrocnt >=2:
                        return [0] *ln
            else:
                mult = mult * nums[i]
                
        for i in range (0, ln):
            if  zrocnt >=1 and nums[i] ==0:
                res.append(mult)
            elif zrocnt >=1 and nums[i] !=0:
                res.append(0)
            else:
                res.append (int (mult/nums[i]))
                
        return res
                            
                    
                    
                    