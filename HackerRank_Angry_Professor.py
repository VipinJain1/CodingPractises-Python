# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:50:07 2021

https://www.hackerrank.com/challenges/angry-professor/problem

@author: VIP
"""

a = [-2,-2,0,-1,2]
k =3

def angryProfessor(k, a):
    # Write your code here
    CallsHappened = 'YES'
    count  =0
    for i in range (len(a)):
        if a[i] <= 0:
            count = count +1
            if count >=k:
                CallsHappened ="NO'"
                return ('NO')
                break

    if CallsHappened =='YES':
        return ('YES')
