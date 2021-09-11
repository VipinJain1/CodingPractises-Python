# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:09:02 2021

@author: VIP
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ln = len(image)
        if ln ==0:
            return None
        res = []
        for i in image:
            x= [j^1 for j in i][::-1]
            res.append(x)
        return res
        
            