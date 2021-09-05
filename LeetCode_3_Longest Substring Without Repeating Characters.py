# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:08:45 2021

@author: VIP
"""
"""
def lengthOfLongestSubstring(s):
    ln = len(s)
    if ln<=1:
       return len(s)
        
    d  = dict()
    longest =0 
    cnt = 0
    start =0
    longeststr = str()
    for j in range (0,ln):
        d = {}
        start = j
        cnt =0
        for i in range (j, ln):
            if s[i] not in d.keys():
                d[s[i]] =1
                cnt +=1
                if longest <cnt:
                    longest = cnt
                    longeststr = s[start:longest]
          
            else:
                if longest <cnt:
                    longest = cnt
                    longeststr = s[start:longest]
                cnt =1
                d = {}
                d[s[i]] =1
                

    return longest
"""
def lengthOfLongestSubstring(s):
    charset = set()
    l =0
    res = 0
    for r in range (len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l +=1
        charset.add(s[r])
        res = max(res, r -l+1)
    return res
        

s = "abcabcbb"
s = "asjrgapa"
s = "wpwkew"
#s ="au"
print (lengthOfLongestSubstring(s))