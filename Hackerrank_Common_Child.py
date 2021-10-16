# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:39:10 2021

@author: VIP
"""


def commonChild(s1, s2):
    # Write your code here
    ln1 = len(s1)
    ln2 = len(s2)
    
    if ln1 ==0 or ln2 ==0:
        return None
    
    d1  = {}
    d2 =  {}
    
    for i in s1:
        if i in d1.keys():
            d1[i] =+1
        else:
            d1[i] =1
    for i in s2:
        if i in d2.keys():
            d2[i] =+1
        else:
            d2[i] =1
    cnt  =0
    for i in d1.keys():
        if i in d2.keys():
            cnt += min (d1[i], d2[i])
    
    return cnt
S1 = 'SHINCHAN'
S2 = 'NOHARAAA'

print (commonChild(S1, S2))