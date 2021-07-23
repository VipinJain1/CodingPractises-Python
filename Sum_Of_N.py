# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/program-find-sum-first-n-natural-numbers/

Program to find sum of first n natural numbers
Difficulty Level : Basic
Last Updated : 08 Apr, 2021
Given a number n, find the sum of first natural numbers.

Examples : 

Input : n = 3
Output : 6
Explanation :
Note that 1 + 2 + 3 = 6

Input  : 5
Output : 15 
Explanation :
Note that 1 + 2 + 3 + 4 + 5 = 15


"""

sum1 = 0
def recSum(n):
    if n ==0:
        return  0
    return n + recSum(n-1)
    
print (recSum(20))
    