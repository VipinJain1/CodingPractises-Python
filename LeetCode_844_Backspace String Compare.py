# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:57:31 2021

@author: VIP
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        start =0
        end = len(s) -1
        stack = []
        while (start <=end):
            if s[start] =="#":
                if len(stack) >0:
                    stack.pop()
            else:
                stack.append(s[start])
            start +=1
            
        start =0
        end = len(t) -1
        stack1 = []
        while (start <=end):
            if t[start] =="#":
                if len(stack1) >0:
                    stack1.pop()
            else:
                stack1.append(t[start])
            start +=1
        print (stack)
        print (stack1)
        if stack == stack1:
            return True
        else:
            return False
        
        
    