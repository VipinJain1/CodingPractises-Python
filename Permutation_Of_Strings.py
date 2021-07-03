# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:31:29 2021
Find Whether Two Strings are Permutation of each other

@author: VIP
"""


A  = "ABCD"
B = "ADBC"

a = dict()
b = dict()
for i in A:
    if i in a.keys():
        a[i] = a[i] +1
    else:
       a[i] =1


for j in B:
    if j in b.keys():
        b[j] = b[j] +1
    else:
        b[j] = 1

flag = True
for i in A:
    if (a[i] != b[i]):
        flag  = False

print (flag)

