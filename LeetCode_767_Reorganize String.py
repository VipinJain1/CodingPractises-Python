# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:15:07 2021

@author: VIP
"""

class Solution:
    def reorganizeString(self, sw: str) -> str:
        s= list(sw)
        ln = len(s)
        cnt =0
        while (cnt<ln):
            j = cnt+1
            while (j< ln):
                if s[cnt] == s[j]:
                    ptr =j
                    while (s[cnt] == s[j]):
                        if j ==ln-1:
                            return "Not Possible"
                        else:
                            j +=1
                           
                    s[ptr], s[j] = s[j], s[ptr]
                    break
                else:
                    j+=1
                    cnt +=1
            cnt +=1        
        return s

s= "ggfdqgwfgwfhrqewrhlrhpruweqweieyrwigfkwlehthhhhghhghhhg"
obj = Solution()
ret = obj.reorganizeString(s)
print (ret)