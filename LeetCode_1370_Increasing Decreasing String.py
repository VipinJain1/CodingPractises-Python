# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:46:18 2021

@author: VIP
"""

class Solution:
    def sortString(self, s1: str) -> str:
        res = []
        ln = len(s1)
        if ln <=1:
            return s1
        s = sorted (set(s1))
        rs = list(s)[::-1]
        if len (s) ==1:
            return s1
        d = {}
        for i in s1:
            if i in d.keys():
                d[i] +=1
            else:
                d[i] =1
                
        cnt =0
        while (cnt<ln):
            for i in s:
                if cnt <ln and d[i] >=1:
                    res.append(i)
                    cnt +=1
                    d[i] -=1
            for j in rs:
                if cnt <ln and d[j] >=1:
                    res.append(j)
                    d[j] -=1
                    cnt +=1
        return  "".join(res) 