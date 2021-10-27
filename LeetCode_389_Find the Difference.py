# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:24:02 2021

@author: VIP
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ln = len(t)
        if ln ==0:
            return
      
        dt = dict()
        ds = dict()
    
        for i in s:
            if i  in ds.keys():
                ds[i] +=1
            else:
                ds[i] =1
    
        for i in t:
            if i  in dt.keys():
                dt[i] +=1
            else:
                dt[i] =1
        found = False
        for key,val in dt.items():
            if key in ds.keys() and dt[key] !=ds[key]:
                found = True
                return key
            elif key not in ds.keys():
                return key
            
                 
        return found     
            
    
s = "giyklhfesfeertwertgrfqwperowqroqegrkeyweyy"
t = "giyklhfesfeertwertgrfqwperowqproqegrkeyweyy"
sol = Solution()
print (sol.findTheDifference(s,t))