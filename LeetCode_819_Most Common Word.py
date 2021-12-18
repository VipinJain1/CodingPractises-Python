# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:34:47 2021

@author: VipLeo
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.split(" ")
        #P = p1.split(',')
        print (p)
        from collections import defaultdict
        d = defaultdict(int)
        for ii in p:
            s  = ii.split(',')
            for i1 in s:
                i1 = i1.lower()
                i = ''.join(filter(str.isalnum, i1))
                #print (i)
                if i not in banned and i.isalpha():
                    d[i] +=1

        import heapq
        
        #print (d)
        largest = heapq.nlargest(1,d.items(), key = lambda x:x[1])
        #print (largest)
        return largest[0][0]
        
                
                
    
    
    
        