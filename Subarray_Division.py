# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:20:49 2021

https://www.hackerrank.com/challenges/the-birthday-bar/problem

@author: VIP
"""

def birthday(s, d, m):
    count =0
    sum = 0
    ln  =  len (s)
    for  i in range (ln):
        sum =0
        for j in range (0,m):
           
           if i+j <ln:
               sum =sum +  s[i+j] 
        if sum  ==  d:
            count += 1
           
    return count 
    
    

s = [2,2,1,3,2]
#s = [1,1,1,1,1,1]
d =4
m =2

print (birthday(s, d, m))

