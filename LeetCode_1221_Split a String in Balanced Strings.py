# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:32:25 2021

https://leetcode.com/problems/split-a-string-in-balanced-strings/

@author: VIP
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = len (s)
        if l <=1:
            return 0
        count  = 0
        foundR = False
        foundL = False
        total  = 0
        countR = 0
        countL = 0
        
        while (count <l):
            if s[count] =='L':
                foundL = True
                countL +=1
            else:
                foundR =  True
                countR +=1
                
            if ((foundL and foundR) and (countR == countL)):
                total +=1
                foundR = False
                foundL = False
                countL = 0
                countR = 0
                
            count +=1
        return total   
            
            
            