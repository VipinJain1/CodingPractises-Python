# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:33:46 2021

@author: VIP
"""
class Solution:
    def secondHighest(self, s: str) -> int:
        res =[]
        s1 =set (s)
      
        for i in set (s):
            if i.isdigit():
                res.append(i)
       
        ln = len(res)
        if ln <=1:
            return -1
        
        return sorted(res)[len(res)-2]
                
            
        
