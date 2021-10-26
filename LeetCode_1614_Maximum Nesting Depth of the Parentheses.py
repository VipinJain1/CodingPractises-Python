# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:10:37 2021

@author: VIP
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        
        ln = len(s)
        if ln ==0:
            return 
        
        stack = []
        cnt  =0
        mxcnt = 0
        for i in s:
            if i in ['(']:
                stack.append(i)
                cnt += 1
            if i in [')']:
                if mxcnt <cnt:
                    mxcnt = cnt
                stack.pop()
                cnt -=1
        return mxcnt
    
                
                
            

            