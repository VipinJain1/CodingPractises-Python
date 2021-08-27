# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:17:06 2021

345. Reverse Vowels of a String
Easy

1169

1579

Add to List

Share
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in bot

https://leetcode.com/problems/reverse-vowels-of-a-string/

@author: VIP
"""

s ="A man, a plan, a canal: Panama"
s ='hello'

s1 = list(s)
v = ['a','e','i','o','u']
l =  len (s) -1
count  =0

while (count <l):
    if s1[count].lower() in v:
       while (l > count):
           if s1[l].lower() in v:
               s1[count], s1[l]=  s1[l], s1[count]
               l = l-1
               count = count +1
               break
           else:
               l = l-1
    else:
       count = count +1 

print ("".join (s1))


