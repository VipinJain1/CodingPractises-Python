# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:48:22 2021

https://www.hackerrank.com/challenges/nested-list/problem

@author: VIP
"""

if __name__ == '__main__':
    import heapq
    od  = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in od.keys():
            od[score].append(name)
        else:
          od[score] = [name]  
    
    l =  list (od.keys())
    heapq.heapify(l)
    p =  (heapq.nsmallest(2,l))[1]
    l = sorted (od[p])
    for i in l:
        print (i)
  
