# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:22:00 2021

14. Longest Common Prefix
Easy

4894

2376

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

https://leetcode.com/problems/longest-common-prefix/

@author: VIP
"""


strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

strs = ["VVVV"]
strs = ["flower","flower","flower","flower"]

if len(strs) ==1:
    print (strs[0])
        
cnt = 1
maxstr = str()
found = True
while (cnt <=len (strs[0])):
    
    st = strs[0][0:cnt]
    for i in strs:
       
        if i[0:cnt] != st:
            found = False
            break
            
            
    if (found == True):
        maxstr = st
    

    if (found == False and cnt ==1):
        print ( "NONE")
        break
    cnt  = cnt+1      
print (maxstr)
        
            
            
        
    
        

    
    
   
    
    
    
