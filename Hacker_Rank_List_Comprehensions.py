# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:01:07 2021
https://www.hackerrank.com/challenges/list-comprehensions/problem

@author: VIP
"""

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b    + c != n ])