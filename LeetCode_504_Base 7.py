# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 08:56:58 2021

@author: VIP
"""

class Solution:
    def convertToBase7(self, orignum):
        
        if orignum <0:
            num = 0 - orignum
        else:
            num = orignum
        res = []
        if num ==0:
            return "0"
        while num:
            res.append(str(num%7))
            num = num//7
        
        resstr =  "".join(res[::-1])
          
        if orignum <0:
            return  ("-" + resstr)
        else:
            return resstr
            
             
            
        