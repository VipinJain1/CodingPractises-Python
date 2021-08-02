# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/picking-numbers/problem

Given an array of integers, find the longest subarray where the absolute 
difference between any two elements is less than or equal to .

@author: VIP
"""

s1 = 'and'
s2 = 'art'

s1 ='be'
s2 =  'cat'

subStr = 'NO'
for i in range (0,len(s1)-1):
    
    for j in range (i+1, len (s1)-1):
        
        if (s1[i:j] in s2):
            print ('YES')
            subStr ='YES'
            break 

if   subStr =='NO':
    print ('NO')      
            
        