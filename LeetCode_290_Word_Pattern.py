# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:37:37 2021

@author: VIP
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list (pattern)
        s =list (s.split(" "))
        lnp = len (pattern)
        lns = len (s)
        if lns != lnp:
            return
        cnt =0
        d ={}
        d1={}
        
        for idx, val in enumerate (pattern):
            if val in d.keys():
                d[val] +=[idx]
            else:
                d[val] =[idx]
            

        for idx, val in enumerate (s):
            if val in d1.keys():
                d1[val] +=[idx]
            else:
                d1[val] =[idx]
        flag = True
        for i in range (0,lnp):
            if d[pattern[i]] != d1[s[i]]:
                flag = False
                return False
        return flag

pattern ="abba"    
s ='dog cat cat dog'
obj = Solution()
print (obj.wordPattern(pattern,s))