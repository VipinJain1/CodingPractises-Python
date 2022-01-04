# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 08:10:57 2021

# Dunamic Knapsack after Memoize 

@author: VIP
"""

def knapsack(a, w,v,n,t):
    
    if w ==0 or n ==0:
        return 0
    
    if t[n][w] !=-1:
        return t[n][w]
    if   a[n-1] <=w:
        t[n][w] =  max (v[n-1] + knapsack(a, w - a[n-1],v,n-1,t) , knapsack(a, w,v,n-1,t))
        return t[n][w]
    else:
        t[n][w] = knapsack(a, w,v,n-1,t)
        return t[n][w]
w =10
a = [2,3,5,6,7,9]
v = [1,4,5,7,5,3]
n = len(a) 
t = [[-1] * (w+1)] * (n+1)
print (knapsack(a,w,v,n,t))
print ('done')

