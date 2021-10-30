# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:32:35 2021

@author: VIP
"""

class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n ==0:
            return False
        k = len(str(n))
        print (k)
        sm =0
        org =n
        while (n):
            d = n%10
            n= n//10
            sm = sm + d**k
      
        if sm ==org: 
            return True
        else:
            return False