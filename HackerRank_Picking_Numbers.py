# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/picking-numbers/problem

Given an array of integers, find the longest subarray where the absolute 
difference between any two elements is less than or equal to .

@author: VIP
"""



a = [1,1,2,3,4,4,5,5,5]

maxnums =0
count=0

for i in range (len(a)-1):
    count =0
    for j in range ( i+1, len(a)-1):
        
        if (abs (a[i] - a[j]) <=1):
            while ((abs (a[i] - a[j]) <=1) and j<= len(a) -1):
                count = count +1
                j= j+1
             
            if maxnums < count:
                maxnums = count
    
        