# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:54:37 2021

@author: VIP
"""
import copy

def palindromeIndex(s):
    # Write your code here
    

    l = list ()
    l = list (s)
    orig = list (s) 
    if l == l[::-1]:
        return -1
 
    for count,i in enumerate(l):
      
        l.pop(count)
     
        if l == l[::-1]:
            return count
        else:
            l = list (orig)
    
    return -1
s ='aaab'
#s= 'aaa'
print (palindromeIndex(s))
