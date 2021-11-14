# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:48:30 2021

@author: VIP
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num1 = '{:032b}'.format(x)
        num2 = '{:032b}'.format(y)
        cnt =0
        for i in range (0, 32):
            if num1[i] !=num2[i]:
                cnt +=1
        return cnt       
        
            
        