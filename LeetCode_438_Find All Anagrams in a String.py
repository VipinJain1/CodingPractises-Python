# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:14:32 2021

@author: VIP
"""
class Solution:
    def findAnagrams(self, s, p):
        lns = len(s)
        lnp = len(p)
     
        if lnp > lns or lns ==0 or lnp ==0:
            return
        
        dp = {}
        ds = {}
        res =[]
        
        for i in p:
            if i in dp.keys():
                dp[i] +=1
            else:
                dp[i] =1
      
        for i in s[0:lnp]:
            if i in ds.keys():
                ds[i] +=1
            else:
                ds[i] =1
        if dp.keys() == ds.keys():
            res.append(0)
            
        for i in range (1,lns-lnp+1):
            if s[i] == s[i+lnp-1]:
                res.append(i)
                continue
            ds[s[i]] -=1    
            if s[i+lnp-1] not in dp.keys():
                continue
            else:
                ds[s[i]] +=1
                if dp.keys()==ds.keys():
                    res.append(i)
            
        return res     
    

s="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy\
zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza\
bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc\
defghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc\
defghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef\
ghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde\
fghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk"
p= "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl"
s= 'cbaebabacd'
p ='abc'
obj = Solution()
res= obj.findAnagrams(s,p)
print (res)