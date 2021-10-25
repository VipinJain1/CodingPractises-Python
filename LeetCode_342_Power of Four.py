# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:19:12 2021

@author: VIP
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n >0 and (n & (n-1) ==0 ) and (n%3 ==1):
            return True
        else:
            return False
            
        
