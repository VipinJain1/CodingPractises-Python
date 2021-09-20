# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:15:21 2021

https://www.hackerrank.com/challenges/any-or-all/problem

@author: VIP
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int (input())
b  =  [int (x)for x in (input()).split(" ")]
if  all (x >0 for x in b) and any (str(x) ==(str(x))[::-1] for x in b ):
    print (True)
    

