# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:07:35 2021

@author: VIP
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ln = len(s)
        if ln <=1:
            return s
        
        if s == s[::-1]:
            return s
            
        cnt  = ln
        while (cnt >=0):
            if s[0:cnt] == (s[0:cnt])[::-1]:
                if cnt <ln:
                    return ((s[cnt:ln])[::-1] + s)
                else:
                    return s
            else:
                cnt -=1
                
            
                
            
            