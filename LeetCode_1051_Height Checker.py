# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:00:11 2021

@author: VIP
"""

class Solution:
 def heightChecker(self, heights: List[int]) -> int:

 ln = len(heights)
 if ln ==0:
 return
 count =0
 h = sorted (heights)
 for i in range (0,ln):
 if h[i] != heights [i]:
 count +=1

 return count 

Sent with a Spark
