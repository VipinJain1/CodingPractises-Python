# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:38:44 2021

https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

@author: VIP
"""

i = 13
j =45
k =3

count =0
for i in range (i,j+1):
    rev = int((str(i))[::-1])
    print (i, rev)
    if ((abs(i-rev)) %k ==0):
        count = count +1

print (count) 
    
