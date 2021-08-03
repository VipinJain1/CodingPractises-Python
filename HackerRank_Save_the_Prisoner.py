# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:32:38 2021

@author: VIP
"""

def saveThePrisoner(n, m, s):
    # Write your code here
    
    
    if (m ==1):
         return (s) 
    if n==0:
        return  0
    
    if s ==0:
        return 0
    
    if n<s:
        return 0 
    
    if n ==m and s==1:
        return s
       
    m = m-1
    while (m >0):
       
        if (s == n):    
            s = 1
            m = m-1
        s = s+1
        m = m-1
    return s    

n = 999999999 
m = 999999999 
s = 1
    
print (saveThePrisoner(n,m,s))