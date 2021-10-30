# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:32:03 2021

@author: VIP
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ln1 =len(word1)
        ln2 = len(word2)
        s = str()
        if ln1 <ln2:
            ln = ln1
        else:
            ln = ln2
        
        print (ln)
        for i in range (0,ln):
            s = s +  word1[i] + word2[i]
        if ln1 ==ln2:
            return s
        elif ln1>ln2:
            return s + word1[ln:]
        else:
            return s + word2[ln:]
        