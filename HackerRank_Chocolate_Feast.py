# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:36:50 2021

https://www.hackerrank.com/challenges/chocolate-feast/problem

@author: VIP
"""

n=43203
c =60
m =5

def chocolateFeast(n, c, m):
    totalBar = n//c
    wrapper = n//c
    
    if n==0 or c ==0 or m ==0:
        return 0
    if c ==1 and m ==1:
        return 2
    while (wrapper >=1): 
        if (wrapper <m):
            return totalBar
        totalBar = int (totalBar + wrapper//m)
        leftover = int (wrapper%m)
        wrapper =  int (wrapper/m)
        wrapper = leftover + ( wrapper) 
    return totalBar

print (chocolateFeast(n,c,m))
    

