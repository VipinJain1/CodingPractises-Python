# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:13:42 2021

@author: VIP
"""


def countConsistentStrings(allowed, words):
    s  = set()
    allowed1  = "".join (sorted (allowed))
    cnt  =0
    
    for i in words:
        s = "".join(sorted (set(i)))
        if s in allowed1:
            cnt +=1
        else:
            for i in s:
                if i in allowed1:
                    found = True
                else:
                    found = False
                    break 
            if found == True:
                cnt +=1

    return cnt

allowed = "ab" 
words = ["a","b","c","ab","ac","bc","abc"]
 
print (countConsistentStrings(allowed,words))          