# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

https://www.hackerrank.com/challenges/picking-numbers/problem

Given an array of integers, find the longest subarray where the absolute 
difference between any two elements is less than or equal to .

@author: VIP
"""

def twoStrings(s1, s2):
    if (set(s1).intersection(set(s2))):
        return 'YES'
    else:
        return "NO"
  
    """  
    subStr = 'NO'
    
    if s1 == s2:
        return 'YES'
    
    if len(s1 )  ==0 or len(s2) ==0:
        return "NO"
        
    for i in range (0,len(s1)-1):
        
        for j in range (i+1, len (s1)-1):
            
            if (s1[i:j] in s2):
                return ('YES')
                subStr ='YES'
                break 
    
    for i in range (0,len(s2)-1):
        
        for j in range (i+1, len (s2)-1):
            
            if (s2[i:j] in s1):
                return ('YES')
                subStr ='YES'
                break 
    
    if   subStr =='NO':
        return ('NO')      
            
"""
    
    
    
s1 ='123444'
s2 = 'art'
s1 ='0 '
s2 =  'cat'

print (twoStrings(s1, s2))