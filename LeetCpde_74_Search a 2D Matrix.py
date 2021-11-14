# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:56:01 2021

@author: VIP
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            print ("I==",i)
            if target >= i[0] and target <= i[len(i)-1]:
                try:
                    val = i.index(target)
                    return True
                except:
                    return False
            