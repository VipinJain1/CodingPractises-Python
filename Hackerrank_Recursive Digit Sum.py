# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:36:47 2021

@author: VIP
"""


def getdata(n, k):
    sm =0
    if int (n) //10 ==0:
        return n
    for i in n:
        sm = sm + int (i)
    return getdata(str (sm), 1) 
    
def superDigit(n, k):
    # Write your code here
    
    n =  str(n)*k
    sm = 0
    ln =len(n)
    if ln ==0:
        return 0
         
    n =  getdata(n, k)
    return n

n =122
k =9


print (superDigit(n, k))
