# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:05:58 2021

@author: VIP
"""
class Solution:
def destCity(self, paths: List[List[str]]) -> str:

    ln   = len(paths)
    if ln ==0:
        return None
    if ln ==1:
        return paths[0][1]
    
    d = {}
    
    for i in paths:
        if i[0] in d.keys():
            d[i[0]] +=1
        else:
            d[i[0]] =1
        if i[1] in d.keys():
            d[i[1]] +=1
        else:
            d[i[1]] =1
    res = []     
    for city, count in d.items():
        if count ==1:
            res.append (city)

    for i in paths:
        if i[1] in res:
            return i[1]