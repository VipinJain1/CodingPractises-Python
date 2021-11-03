# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:29:42 2021

@author: VIP
"""

    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cnt =0
        ln = len(s)
        if ln <3:
            return None
        res =[]
        while (cnt<ln-1):
            newcnt = 1
            if (s[cnt] == s[cnt+1]):
                start =cnt

                while s[cnt] == s[cnt+1]:
                    newcnt +=1
                    cnt +=1
                    if cnt >= ln-1:
                        break
                    
            if newcnt >=3:
                res.append([start, start+newcnt-1])
       
            cnt +=1
        return res 
            
                