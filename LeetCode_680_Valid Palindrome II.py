# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:43:36 2021

@author: VIP
"""

class Solution:
    def isPalindrome(self,s,start,end):
        while (start<end):
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        flag = False
        cnt =0
        ln = len(s) -1
        if ln <=1:
            return True
        
        while (cnt <ln):
            if (s[cnt] != s[ln]):
                return (self.isPalindrome(s,cnt+1,ln) or self.isPalindrome(s,cnt,ln-1))
                        
            cnt +=1
            ln -=1
            
        return True
    