# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:16:49 2021

@author: VIP
"""

#FIXME#  Not Working 
def findSubstring(s, words):
    
    ls = len(s)
    lw = len(words)
    if ls ==0 or lw ==0:
        return
    res = set()
    
    sizew = len(words[0])
    totalsizeW = sizew*lw
    if ls < totalsizeW:
        return []
    start = None
    end = None
    
    for i in words:
        for j in range (0,ls,sizew):
            string = s[j:]
            try:
                start = string.index(i)
            except Exception:
                pass
      
            if start ==None:
                return []
            end = start + totalsizeW
            found = True
            d = dict()
            for i in words:
                if i not in s[start:end]:
                    found  = False
                    break
                else:
                    loc = s[start:end].index(i)
                    if loc not in d.keys():
                        d[loc]= i
                    elif loc in d.keys():
                        found = False
                        break
                    
            if found == True:
                res.add(start)
    return list (res)

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
s = "barfoofoobarthefoobarman"
words = ["foo", "bar"]
print (findSubstring(s, words))