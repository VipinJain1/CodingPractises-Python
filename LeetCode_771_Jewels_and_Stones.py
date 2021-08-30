# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:32:39 2021

https://leetcode.com/problems/jewels-and-stones/

@author: VIP
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ln = len(stones)
        if ln ==0:
            return None
        if len(jewels) == 0:
            return None
        
        count =0
        for i in  stones:
            if i in jewels:
                count = count +1
           
        return count
    
        