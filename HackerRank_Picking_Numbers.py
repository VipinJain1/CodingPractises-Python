# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/picking-numbers/problem

Given an array of integers, find the longest subarray where the absolute 
difference between any two elements is less than or equal to .

@author: VIP
"""


a = [1,1,2,2,4,4,5,5,5]

def pickingNumbers(a):
    # Write your code here

    ln = len (a)
    count  =1
    for i in range (0,len(a)):
        if (abs(a[i]  - a[i+1]) <=1):
            count  = count +1
        else:
            if (len(a[0:count]) > len (a[count:ln])):
                return  len(a[0:count])
            else:
                return  len (a[count:ln])
    return count
        
print (pickingNumbers(a))