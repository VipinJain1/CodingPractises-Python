# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:45:24 2021

https://leetcode.com/problems/reverse-string/

@author: VIP
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        if l  <=1:
            return s
        l1 =l-1
        i =0
        while i <l1:
            s[i], s[l1] = s[l1] , s[i]
            l1 = l1-1
            i = i+1
        return s
            