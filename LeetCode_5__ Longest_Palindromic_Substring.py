# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:24:57 2021

https://leetcode.com/problems/longest-palindromic-substring/submissions/

@author: VIP
"""


def longestPalindrome(s):
    ln = len(s)
    
    found = False
    
    if ln==0:
        return None
    if ln ==1:
        return s
    mxln = 0    
    newstr = str()
    for i in range (0,ln):
        count  = ln -1
        
        while (count > i):
            if s[i] == s[count] and count >i:
                new = s[i:count+1]
                if new == new[::-1]:
                    found = True
                    newln = len(new)
                    if mxln <newln:
                        mxln = newln
                        newstr = new
                    
            count = count -1
    
    if found == False:
        return s[0]
      
    return newstr


s = "aacabdkacaa"

print (longestPalindrome(s))
    
    
    
    
        
    