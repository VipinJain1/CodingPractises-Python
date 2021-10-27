# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:18:19 2021

@author: VIP
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ln = len (s)
        ls = len (t)
        
        if ln == 0 or ls ==0:
            return
        
        if ln !=ls:
            return False
        ds ={}
        dt ={}
        for idx, val in enumerate(s):
            if val in ds.keys():
                ds[val] += [idx]
            else:
                ds[val] = [idx]
        for idx, val in enumerate(t):
            if val in dt.keys():
                dt[val] += [idx]
            else:
                dt[val] = [idx]
                
        print (ds)
        print (dt)
        if list (ds.values()) == list (dt.values()):
            return True
        else:
            return False
        
            
        
        