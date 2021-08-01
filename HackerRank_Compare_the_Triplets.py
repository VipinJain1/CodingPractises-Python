# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:43:40 2021
https://www.hackerrank.com/challenges/compare-the-triplets/problem

@author: VIP
"""


a =[5, 6, 7] 
b = [3, 6, 10]
acnt =0
bcnt =0
print (a,b) 
if (a[0] > b[0]):
    acnt = acnt+1
elif  (a[0] < b[0]): 
    bcnt = bcnt+1
if (a[1] > b[1]):
    acnt = acnt+1
elif  (a[1] < b[1]): 
    bcnt = bcnt+1
    
if (a[2] > b[2]):
    acnt = acnt+1
elif  (a[2] < b[2]): 
    bcnt = bcnt+1

print (acnt, bcnt)
