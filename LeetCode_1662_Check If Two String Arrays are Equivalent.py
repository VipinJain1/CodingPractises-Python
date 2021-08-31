# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:51:03 2021

@author: VIP
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''.join (word1)
        w2 =  ''.join (word2)
        print (w1)
        print (w2)
        if w1 ==w2:
            return  True
        else:
            return False