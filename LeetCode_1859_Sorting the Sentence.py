# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:53:02 2021

https://leetcode.com/problems/sorting-the-sentence/

@author: VIP
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        
        ln = len(s)
        if ln <=1:
            return s
        d = dict()
        count =0
        for i in (s.split(' ')):
            d[i[len(i) -1]]  = i[0:len(i)-1]
            count +=1
            
        cnt  =1
        d1 = []
        print (d) 
        while cnt <=count:
            cnt = str(cnt)
            d1.append (d[cnt])
            cnt = int (cnt)
            cnt +=1
        
        return " ".join(d1)
                  
                  