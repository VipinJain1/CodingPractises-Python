# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 23:05:04 2021
https://leetcode.com/problems/single-number-ii/

@author: VIP
"""

import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln ==0:
            return 0
        if ln ==1:
            return nums[0]
        
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        for key, val in d.items():
            if val == 1:
                return key
          