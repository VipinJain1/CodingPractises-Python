# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:42:19 2021

@author: VIP
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = ['a','i','e','o','u']
                  
        ln  = len(s)/2
        cnt1 =cnt2 =0
        cnt =0          
        
        for i in s:
            if i.lower() in vovels:
                if cnt <ln:
                    cnt1 +=1
                else:
                    cnt2 +=1
            cnt +=1
        if cnt1 == cnt2:
            return True
        else:
            return False
                  
                 
                  
                  