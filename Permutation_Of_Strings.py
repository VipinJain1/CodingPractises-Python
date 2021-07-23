# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:31:29 2021
Find Whether Two Strings are Permutation of each other

@author: VIP

https://www.geeksforgeeks.org/check-if-two-strings-are-permutation-of-each-other/

Check if two strings are permutation of each other

Write a function to check whether two given strings are Permutation of each other or not. 
A Permutation of a string is another string that contains same characters, only the order of characters can be different. 
For example, “abcd” and “dabc” are Permutation of each other

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

