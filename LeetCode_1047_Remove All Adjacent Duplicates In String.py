# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:08:36 2021

@author: VIP
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]
        for ch in s:
            if stack and stack[-1] ==ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
            
       