# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:40:37 2021

@author: VIP
"""

def cookies(k, A):
    # Write your code here
    val = 0 
    A = sorted(A)
    count = 0  
   
    while ( True):
        
        if all ( y > k for y in A):
            return count
        
        count += 1
        val = 1*A[0] + 2* A[1]
        A  = A[2:]
        A.append(val)
        A  = sorted (A)
        if len (A) ==0:
           return  -1
        if len (A) ==1 and A[0] < k:
           return -1 

k  = 7
A = [1,2,3,9,10,12]

print(cookies(k, A))