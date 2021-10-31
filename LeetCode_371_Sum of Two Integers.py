# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:45:45 2021

@author: VIP
"""

class Solution:
 def getSum(self, a: int, b: int) -> int:

 if a==0:
 return b
 if b ==0:
 return a
 if a ==0 and b==0:
 return 0

 if a>=0 and b>0:
 for i in range (0,b):
 a+=1
 return a
 elif a<0 and b<0:
 for i in range (0,abs (b)):
 a-=1
 return a

 elif a>0 and b<0:
 for i in range (0,abs(b)):
 a-=1
 return a
 elif a <0 and b>0:
 for i in range (0,abs(a)):
 b-=1
 return b
