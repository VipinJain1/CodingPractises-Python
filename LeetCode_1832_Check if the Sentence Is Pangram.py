# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:57:44 2021

@author: VIP
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string
        found  = True
        s = string.ascii_lowercase
        for i in s:
            if i not in sentence:
                found = False
                return False
        return found    
        