# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 00:14:22 2021

https://www.hackerrank.com/challenges/find-digits/problem

An integer  is a divisor of an integer  if the remainder of .

Given an integer, for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer.

@author: VIP
"""


n =1012

count  =0
for i in str(n):
    if int (i) != 0:
        
        if n%int (i)  ==0:
            count = count +1
print (count)