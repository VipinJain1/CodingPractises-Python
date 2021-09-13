# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:15:03 2021

@author: VIP
"""

def findTheDifference(s,t):
 
    ls = len(s)
    lt = len (t)
    
    s1  =[]
    t1  =[]
    s1[:] = (s)
    print (s1)
  
    t1[:] =  (t)
    print (t1)
    
    print (t1[ls:])
    return "".join(t1[ls:])
    
    

s= ""
t ='z'
print (findTheDifference(s,t))