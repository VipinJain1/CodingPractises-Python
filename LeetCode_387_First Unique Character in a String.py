# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 22:14:34 2021

@author: VIP
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        found = False
        l  = len (s)
        if  l  <=1:
            return 0
        d  = {}
        for i  in s:
            if  i in d.keys():
                d[i] +=1
            else:
                d[i] =1
        lst =[]
        lst[::] = s
        for i in range (0,l):
            if d[lst[i]] ==1:
                found = True
                return i
        
        if found == False:
            return -1