# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:22:05 2021

@author: VIP
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.res = nums
        #print (self.res)
      
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.res[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)