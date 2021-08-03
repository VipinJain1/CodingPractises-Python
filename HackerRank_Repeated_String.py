# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:29:34 2021

https://www.hackerrank.com/challenges/repeated-string/problem

@author: VIP
"""

s ='abaSbaba'
n =20

def repeatedString(s, n):
    # Write your code here
    
    if ((n ==0 ) or ('a' not in s)):
        return 0
    
    l = len(s) 
    if ((l == 1) or (len (set(s)) == 1)) :
        return n
    
    count =0
    for i in s:
        if i =='a':
            count = count +1

    dv = n//l
    totalcnt = dv*count
    left  = n%l
    
    for i in s[0:left]:
        
        if i =='a':
            totalcnt = totalcnt+1
            
    return totalcnt
            

print (repeatedString(s,n))