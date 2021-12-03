# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:56:22 2021

@author: VIP
"""

class Solution:
    from collections import Counter
    
    def getCGD(self,x,y):
            while (y):
                x,y=y,x%y
            return x
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        ln = len(deck)
        if ln <=1:
            return False
        
        d = Counter(deck)
        gcd =0
        for i in d.values():
            gcd = self.getCGD(gcd,i)
            if gcd ==1:
                return False
        return True
        