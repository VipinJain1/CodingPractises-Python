# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:27:06 2021

@author: VIP
"""

def pageCount(n, p):
    # Write your code here
    
    start = 0
    end = 0
    
    if p > n:
        return 0
    if  n-1 == p or n-2  ==p or p ==1:
        return  0
    else:
        end = (n -p)//2
        start = (p-1)//2 +1
    if end <start:
        return end
    else: 
        return start
        

n =5
p =4
print (pageCount(n,p))