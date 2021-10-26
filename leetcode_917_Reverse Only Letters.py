# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:14:58 2021

@author: VIP
"""

class Solution:
 def reverseOnlyLetters(self, s: str) -> str:

 ln = len(s)
 if ln ==0:
 return False

 s = list (s[:])

 start =0
 end = ln -1
 while (start < end):
 while (s[start].isalpha() and s[end].isalpha() and start<end):
 s[start], s[end] = s[end], s[start]
 end = end -1
 start = start +1
 if s[start].isalpha() != True:
 start +=1
 if s[end].isalpha() != True:
 end -=1

Sent with a Spark
