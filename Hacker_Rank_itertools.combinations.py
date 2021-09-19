# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 08:39:44 2021
https://www.hackerrank.com/challenges/itertools-combinations/problem

@author: VIP
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))