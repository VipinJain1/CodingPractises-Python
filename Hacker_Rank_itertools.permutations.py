# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:30:25 2021

https://www.hackerrank.com/challenges/itertools-permutations/problem

@author: VIP
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

a, b = (input()).split(" ")
l =  sorted (permutations (a,int (b)))

for i in l:
    print ("".join(i)) 



