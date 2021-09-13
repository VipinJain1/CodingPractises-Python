# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 10:52:07 2021

@author: VIP
"""


def countPrimes(n: int) -> int:
    res  = []
    
    if n >3:
        res.append(1)
        res.append (3)
    
        if n ==1:
            return 1
        
    if n <=4:
        return [1,3]
    
    for i in range (4,n):
        
        