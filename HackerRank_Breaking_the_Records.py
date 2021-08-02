# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:08:07 2021

https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

@author: VIP
"""


def breakingRecords(scores):
    # Write your code here
    
    mx = scores [0]
    mn = scores [0]
    maxcnt = 0
    mincnt =0
    count  =1
    ln  = len(scores)
    start  = scores[0]
    
    while (count <ln):
        if scores[count] > mx:
            maxcnt = maxcnt+1
            mx =  scores[count]
        
        if  scores[count] < mn:
            mincnt = mincnt+1
            mn =  scores[count]
        
        count = count +1
    
    return (maxcnt,mincnt)
            
      
scores = [3, 4, 21, 36, 10, 28, 35, 5,24, 42]
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print (breakingRecords(scores))