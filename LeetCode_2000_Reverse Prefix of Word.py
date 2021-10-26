# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:53:19 2021

@author: VIP
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ln = len(word)
        if ln ==0:
            return
        lst = list(word)
        try:
            idx= lst.index(ch)
        except:
            return word
        
        newlst = []
        
        newlst.extend(lst[0:idx+1][::-1])
        newlst.extend(lst[idx+1:ln])
        return "".join(newlst)