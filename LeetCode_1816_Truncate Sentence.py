# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:45:43 2021

@author: VIP
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ln  =len (s)
        if ln ==0 or ln < k:
            return False
        l =[]
        l = s.split(" ")
        return  (" ").join(l[0:k])
        #print (l)

    
        