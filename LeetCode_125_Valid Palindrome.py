# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:08:29 2021

@author: VIP
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ln  = len (s)
        if ln ==0:
            return None
        s1 = str()
        for i in s:
            if i.isalnum():
                s1 = s1+i.lower() 
        print (s1) 
        
        if s1 == s1[::-1]:
            return True
        else:
            return False
        