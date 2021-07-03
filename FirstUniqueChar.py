# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:55:33 2021

@author: VIP
"""

A =  "VVipin"

for i in range(len(A)):
     if A[i] not in list (A[i+1:] + A[:i]):
         print (A[i])
         break






