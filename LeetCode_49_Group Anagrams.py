# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:24:02 2021

@author: VIP
"""


def groupAnagrams(strs):
    
    ln  = len(strs)
    if ln <=1:
        return [strs]
    d = {}
    for i  in strs:
        s = "".join (sorted (i))
        if s in d.keys():
            d[s].append(i)
        else:
            d[s] = [i]
        
    return d.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]

print (groupAnagrams(strs))