# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:41:46 2021

@author: VIP
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0 for i in range(len(s))]
        for i in range(len(s)):
            res[indices[i]] = s[i]
            
        return ''.join(res)
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print (restoreString(s, indices))