# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:21:12 2021

@author: VIP
"""

class Solution:
 def reorderedPowerOf2(self, n: int) -> bool:
 import itertools
 lst = list (str(n))
 ln = len(lst)

 found = False
 if ln ==0:
 return False
 if n & (n-1)==0:
 return True

 if n ==1:
 return True
 totalList= itertools.permutations(lst,ln)
 for i in totalList:
 if i[0]=='0':
 continue

 nm = int ("".join(i))
 if (nm&nm-1 ==0):
 found = True
 return True
 return found

