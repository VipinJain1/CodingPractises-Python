# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:33:39 2021

@author: VIP
"""

def commonChild(s1, s2):
    l1 = []
    l2 = []
    for i in s1:
        if i in s2:
           l1.append(i)
           
    for i in s2:
        if i in s1:
           l2.append(i)
           
    print (l1)
    print (l2)
  
    l3 = []
    count =0
    ###FIXME###
    if l1 ==l2:
        return len(l1)
      
s1 = 'HARRY'
s2 = 'SALLY'
s1 = 'ABCDEF'
s2 = 'FBDAMN'

print (commonChild(s1,s2))
    
