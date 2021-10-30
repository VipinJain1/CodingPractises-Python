# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:27:57 2021

@author: VIP
"""

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        
        res = []
        d = dict()
        s = licensePlate.lower()
        for i in s:
            if i in d.keys() and i.isalpha():
                d[i] +=1
            elif i.isalpha() :
                d[i] =1
        for w in words:
            d1 = dict()
            for i in w:
                if i in d1.keys():
                    d1[i] +=1
                else:
                    d1[i] = 1
            found =True
            for key in d.keys():
                if key in d1.keys():
                    if d[key] >d1[key]:
                        found = False
                        break
                        
                else:
                    found = False
                    continue
            if found == True:
                res.append (w)
        if len(res) ==0:
            return None
        else:
            return min(res, key =len)
                
                