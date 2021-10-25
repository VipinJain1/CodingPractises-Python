# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:30:32 2021

@author: VIP
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <1:
            return False
        
        while (n%3 ==0):
            n = n/3
        
        if n ==1:
            return True
        else:
            return False
        
        
