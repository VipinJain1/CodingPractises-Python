# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 08:25:11 2021

@author: VIP
"""
##Understand the code again even if it works
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ls = len(s)
        lp = len(p)
        if lp==0 or ls==0 or lp >ls:
            return []
        dp ={}
        ds = {}
        result = []
        
        for i in p:
            if i in dp.keys():
                dp[i] +=1
            else:
                dp[i] =1
        
        for i in s[0:lp]:
            if i in ds.keys():
                ds[i] +=1
            else:
                ds[i] =1
        cnt =int () 
        
        if lp ==ls and ds == dp:
            return [0]
        
        for i in range (0,ls-lp):
            if ds ==dp:
                result.append(i)
        
            ds[s[i]] -=1
            if ds[s[i]] ==0:
                ds.pop(s[i])
            if s[i+lp] in ds.keys():
                ds[s[i+lp]] +=1
            else:
                ds[s[i+lp]] =1    
            cnt =i 
        
        if ds ==dp:
            print (cnt+1)
            result.append(cnt+1)
  
        return result
                
                
            
            
                
s = "ab"
p ="ba"
obj = Solution()
res = obj.findAnagrams(s,p)
print (res)