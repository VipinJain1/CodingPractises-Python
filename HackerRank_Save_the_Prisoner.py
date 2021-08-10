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
    
    if n <s:
        return 0
    m = m-1
    while (m >0):
       
        if (s == n):    
            s = 1
            m = m-1
        else:
            s = s+1
            m = m-1
    return s    


n = 5
m = 2
s = 1 
    
print (saveThePrisoner(n,m,s))