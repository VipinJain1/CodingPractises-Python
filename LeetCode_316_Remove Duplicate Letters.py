# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:05:37 2021

@author: VIP
"""

class Solution:
    def removeDuplicateLetters(self, st: str) -> str:
        d = {}
        s = list(st)
        for i in s:
            if i in d.keys():
                d[i][0] +=1
            else:
                d[i] = [1,0]
        print (d)
        print (s)
        cnt =0
        ln = len(s)
        while (cnt<ln):
            elem  = s[cnt]
            if elem in d.keys():
                if d[elem][0] >=1:
                    s.remove(elem)
                    d[elem][0] -=1
                else:
                    cnt +=1
                    
        return "".join(s)         
                
                
        
arr = 'cbacdcbc'
obj = Solution()
res = obj.removeDuplicateLetters(arr)
print (res)