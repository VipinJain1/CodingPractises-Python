# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/sock-merchant/problem

There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

@author: VIP
"""

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

socksDict = {}

for i in range (len(ar)):
    if ar[i] in socksDict.keys(): 
        socksDict[ar[i]] =  socksDict[ar[i]] +1
    else:
        socksDict[ar[i]] =1

count =0
for sock, pair in socksDict.items():
    count = count +pair//2

print (count)     