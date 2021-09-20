# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:23:50 2021

@author: VIP
"""

def combinationSum2(candidates, target):
    from itertools import combinations
    ln  = len(candidates)
    if ln ==0:
        return []
    
    if ln ==1 and candidates[0] == target:
        return [candidates]
    elif ln ==1:
        return []
    res = dict()
    for i in range (1,ln+1):
        l = combinations(candidates,i)
      
        for j in l:
            k = sorted(j) 
            if sum(k) ==target:
                res[tuple(k)] =1
    return list(res.keys())



l= [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
k =27

print (combinationSum2(l,k))