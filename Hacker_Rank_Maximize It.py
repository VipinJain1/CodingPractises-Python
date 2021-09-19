# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 09:22:38 2021
https://www.hackerrank.com/challenges/maximize-it/problem

@author: VIP
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b = (input()).split(" ")
a = int (a)
b = int (b)
ip =[[]]

for i in range (0,a):
    ip.append (list (map (lambda x:int (x), (input().split (" ")))))

totalmx = 0

for i in ip:
    if len(i) >0:
        mx = (max(i[1:]))
        totalmx = totalmx + mx**2

print (totalmx %b)