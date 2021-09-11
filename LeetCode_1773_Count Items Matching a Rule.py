# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:23:14 2021

@author: VIP
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        cnt  =0
        
        ln = len (items)
        if ln  ==0:
            return 0
        
        d =  {'type':0, 'color':1, 'name':2}
        key = d[ruleKey]
        print (key)
        for i in items:
            print (i)
            if i[key]  == ruleValue:
                cnt +=1
        return cnt    
        
        
        
        