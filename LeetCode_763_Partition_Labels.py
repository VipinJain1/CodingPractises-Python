# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:22:03 2021

@author: VIP
"""

class Solution:

    def partitionLabels(self, s: str):
        ln = len(s)
        if ln ==0:
            return []
        d ={}
        for idx, val in enumerate (s):
            if val in d.keys():
                d[val] +=  [idx]
            else:
                d[val] = [idx]
        res =[]
        i =0
        visited = []
        while (i<ln):
            mx = max(d[s[i]])
            visited.append(s[i])
            for j in set (s[i+1:mx]):
                if j not in visited:
                    visited.append(j)
                    if  mx <= max(d[j]):
                        mx = max(d[j])
            i = mx
            res.append(mx+1)
        result =[]    
        for cnt,i in enumerate (res):
            if cnt ==0:
                result.append(res[0])
            else:
                result.append(i -res[cnt-1])
        return result 
        
            
      

s = "ababcbacadefegdehijhklij"
s= 'eccbbbbdec'
s ="qiejxqfnqceocmy"
obj =  Solution()
print (obj.partitionLabels(s))