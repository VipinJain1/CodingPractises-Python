# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:32:38 2021

@author: VIP
"""

def saveThePrisoner(n, m, s):
    # Write your code here
    
    # n - Prisoner - total number of chairs
    # m - number of candies
    # s -  starting chair
    
    if (m ==1):
         return (s) 
    
    if m<1:
         return 0
    if n <=0:
        return  0
    
    if s <=0:
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

n = 7
m = 19
s = 2
    
print (saveThePrisoner(n,m,s))