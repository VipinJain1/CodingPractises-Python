# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:55:14 2021

@author: VIP
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd =0
        even =0
        for i in position:
            if i%2==0:
                even +=1
            else:
                odd +=1
        return  min(odd,even)
        