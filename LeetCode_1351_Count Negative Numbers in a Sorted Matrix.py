# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:00:35 2021

@author: VIP
"""

class Solution:
 def countNegatives(self, grid: List[List[int]]) -> int:

 ln = len(grid)
 if ln ==0:
 return 0
 cnt =0
 for i in grid:
 for j in i:
 if j <0:
 cnt+=1
 return cnt
