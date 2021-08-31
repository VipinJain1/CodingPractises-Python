# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:49:14 2021

@author: VIP
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = dict()
        for i in moves:
            if i in d.keys():
                d[i] = d[i] +1
            else:
                d[i] = 1
        
        if 'D' not in d.keys():
            d['D'] =0

        if 'U' not in d.keys():
            d['U']=0
            
        if 'L' not in d.keys():
            d['L'] =0
        if 'R' not in d.keys():
            d['R'] =0
            
        print (d)
        if ( (d['U'] == d['D']) and (d['R'] == d['L']) ):
            return True
        else:
            return False
            
            
        
        