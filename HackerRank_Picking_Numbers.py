# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/picking-numbers/problem

Given an array of integers, find the longest subarray where the absolute 
difference between any two elements is less than or equal to .

@author: VIP
"""


a = [1,1,2,3,4,4,5,5,5]
a =[4, 6, 5, 3, 3, 1]

def pickingNumbers(a):
    # Write your code here
    
    count =1 
    ln = len(a)
    longest =0
    while (count <=ln):
        if abs(sum (a[0:count]) - sum (a[count+1:ln-1]))  <=1:
             if len(a[count+1:ln-1]) > len(a[0:count]):
                 longest = len(a[count+1:ln-1])
             else:
                 longest = len(a[0:count])
        
        count  = count +1    
        
    return longest 
            
    

print (pickingNumbers(a))