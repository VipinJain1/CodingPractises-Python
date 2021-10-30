# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:33:34 2021

@author: VIP
"""

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ln = len(keyboard)
        if ln==0:
            return None
        sm =0
        prev =0
        for i in word:
            try:
                loc = keyboard.index(i)
                sm = sm + abs(loc - prev)
                prev = loc
            except:
                return None
            
        return sm
