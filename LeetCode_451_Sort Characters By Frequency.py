# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:46:17 2021

@author: VIP
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        
        data  = list(s)
        ln = len(s)
        d = dict()
        for i in data:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] =1
                
        op = heapq.nlargest(ln,d.items(), key = lambda x:x[1])
        #print (op)
        s = str()
        for i in op:
            s = s+ (i[0] *i[1])
        return s

obj = Solution()
s = 'Aabb'
print (obj.frequencySort(s))